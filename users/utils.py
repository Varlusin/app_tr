from grups.models import PopularityCompany, Company
from django.db.models import  When, Case
from django.utils.translation import gettext as _
from django.contrib.auth import authenticate

def autentic(request, login, pw):
    """ Օգտվողին գրանցելու ֆունկցիա """
    lgin= request.POST.get(login)
    psw = request.POST.get(pw)
    user = authenticate(request, email=lgin, password= psw)
    return user


class GetCompanyUserPost:

    def __init__(self, request, slug):
        self.slug = slug
        self.user = request.user

    def get_company_post(self):
        """հետ է վերադարցնում հարցում որը պարունակում է օգտագօրծողների կարծիքները կոնկրետ 
        ընկերության վերաբերյալ բոլոր արժեքները  """
        posts = (
        PopularityCompany.objects
        .select_related('company')
        .filter(company__slug =self.slug)
        .select_related('user')
        .order_by('-pk')
        )
        return posts
    def get_company_user_post(self):
        """հետ է վերադարցնում հարցում dict որտող նեռարված են submit փոփոխել կամ ավելացնել
         և կարծիքների ցուցակը։ """
        posts = self.get_company_post()
        if posts.exclude():
            if  self.user.is_authenticated:
                posts =posts.order_by(
                    Case(When(user = self.user, then = 0), default=1), '-pk').values(
                        'user__id', 'gnahatakan', 'post', 
                        'user__first_name', 'user__last_name')
                post = list(posts)

                if post[0]['user__id']== self.user.id:
                    userpost= { 'post' : post[0], 'slug': self.slug,}
                    post.pop(0)
                    context = {
                        'userpost': userpost,
                        'submit': _('Փոփոխել'),
                        'posts': post,
                        }
                    return context
        posts = posts.values( 'gnahatakan', 'post', 'user__first_name', 'user__last_name')
        context = {
                    'submit': _('ավելացնել'),
                    'slug':self.slug,
                    'posts':posts}
        return context
    



class CalculateRatingCompany:
    """ Ընկերությունների վարքանիշի միջինն հաշվարկը ըստ ոգտվողների գնահատականի """
    def __init__(self, slug, new_rating, old_rating = 0) -> None:
        self.slug = slug
        self.new_rating = new_rating
        self.old_rating = old_rating 

    def get_count_post(self):
        countpost = PopularityCompany.objects.filter(company__slug=self.slug).count()
        rating = Company.objects.filter(slug = self.slug)[0]
        return countpost, rating
    
    def calculate_rating_new_post(self):
        """ նոր գնահատականների դեպքում միջին արժեքի հաշվարկը։ """
        countpost, rating = self.get_count_post()
        new_popularity = (rating.popularity*(countpost) + self.new_rating)/(countpost+1)
        rating.popularity=new_popularity
        rating.save( update_fields =  ['popularity'])

    def ubdate_rating(self):
        """ Գնահատականի փոփոխման դեպքում միջինի թարմացում  """
        countpost, rating = self.get_count_post()
        new_popularity =  rating.popularity + (self.new_rating - self.old_rating)/(countpost+1)
        rating.popularity=new_popularity
        rating.save( update_fields =  ['popularity'])
    def delate_rating(self):
        countpost, rating = self.get_count_post()
        new_popularity = (rating.popularity * (countpost+2) - self.old_rating)/(countpost +1)
        rating.popularity = new_popularity
        rating.save(update_fields = ['popularity'])

