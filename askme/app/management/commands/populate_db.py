import random

from django.core.management.base import BaseCommand, CommandError
from app.models import Question, User, Answer, Tag

class Command(BaseCommand):
    help = 'Populating db with some data'

    def handle(self, *args, **options):

        u = User.objects.create(
            username="custom_user"
        )

        t1 = Tag.objects.create(
            text="question"
        )
        t2 = Tag.objects.create(
            text="StupidQuestion"
        )
        t3 = Tag.objects.create(
            text="tag"
        )

        tags = [t1, t2, t3]

        qN = random.randint(100, 200)
        
        for i in range(qN):
            aN = random.randint(0, 130)
            p = Question(
                user=u,
                title="CoolQuestion"+str(i+1),
                text="At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat.",
                answers=aN,
                rating=random.randint(0, 600)
            )
            p.save()
            tN = random.randint(1, 3)
            for tag_index in range(tN):
                p.tag.add(tags[tag_index])

            for j in range(aN):
                a = Answer.objects.create(
                    question=p,
                    text="Answer"+str(j+1),
                    rating=random.randint(0, 500)
                )
         
#        p1 = Question(
#            user=u,
#            title="CoolQuestion",
#            text=""
#            answers=3,
#            rating=200,
#        )
#        p1.save()
#        p1.tag.add(t1, t2)
#
#        a = Answer.objects.create(
#            question=p1,
#            text="My answer1",
#            rating=1,
#        )
#        a = Answer.objects.create(
#            question=p1,
#            text="My answer2",
#            rating=1,
#        )
#        a = Answer.objects.create(
#            question=p1,
#            text="My answer3",
#            rating=1,
#        )
#
#        p2 = Question.objects.create(
#            user=u,
#            title="CoolQuestion2",
#            answers=2,
#            rating=1,
#        )
#        p2.tag.add(t3)
#
#        a = Answer.objects.create(
#            question=p2,
#            text="My answer3",
#            rating=1,
#        )
#        a = Answer.objects.create(
#            question=p2,
#            text="My answer3",
#            rating=1,
#        )
           
        self.stdout.write(self.style.SUCCESS('Successfully populated DB!'))
