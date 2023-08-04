from django.db import migrations

class Migration(migrations.Migration):
    
    dependencies = [
        ('missions', '0001_initial'),
    ]

    def seed_reviewers(apps, schema_editor):
        Reviewer = apps.get_model('missions', 'Reviewer')
        reviewers = [
            Reviewer(name="John Smith"),
            Reviewer(name="Emily Davis"),
            Reviewer(name="James Lee"),
            Reviewer(name="Sarah Johnson"),
            Reviewer(name="Daniel Kim"),
            Reviewer(name="Michelle Rodriguez"),
            Reviewer(name="Michael Brown"),
            Reviewer(name="Ashley Martinez"),
            Reviewer(name="Robert Baker"),
            Reviewer(name="Julia Garcia"),
            Reviewer(name="William Wilson"),
            Reviewer(name="Lauren Rodriguez"),
            Reviewer(name="Matthew Davis"),
            Reviewer(name="Samantha Lee"),
            Reviewer(name="Gabriel Martinez"),
            Reviewer(name="Sophie Johnson"),
            Reviewer(name="Andrew Kim"),
            Reviewer(name="Olivia Smith"),
            Reviewer(name="Isabella Brown"),
            Reviewer(name="Ethan Garcia"),
            Reviewer(name="Ava Johnson"),
            Reviewer(name="Mia Wilson"),
            Reviewer(name="Noah Rodriguez"),
            Reviewer(name="Liam Martinez"),
            Reviewer(name="Emma Lee"),
            Reviewer(name="Aiden Davis"),
            Reviewer(name="Charlotte Kim"),
            Reviewer(name="Harper Wilson"),
            Reviewer(name="Lucas Brown"),
            Reviewer(name="Evelyn Garcia"),
            Reviewer(name="Logan Johnson"),
            Reviewer(name="Elijah Davis"),
            Reviewer(name="Ella Lee"),
            Reviewer(name="Daniel Martinez"),
            Reviewer(name="Michael Johnson"),
            Reviewer(name="Madison Brown"),
            Reviewer(name="Elizabeth Kim"),
            Reviewer(name="Henry Wilson"),
            Reviewer(name="Sofia Rodriguez"),
            Reviewer(name="Alexander Davis"),
            Reviewer(name="Avery Martinez"),
            Reviewer(name="Benjamin Hernandez"),
            Reviewer(name="Sophia Nguyen"),
            Reviewer(name="Lucy Thompson"),
            Reviewer(name="Caleb Anderson"),
            Reviewer(name="David Wright"),
            Reviewer(name="Chloe Taylor"),
            Reviewer(name="Natalie Wilson"),
            Reviewer(name="Emma Hernandez"),
            Reviewer(name="Avery Wright")
        ]
        Reviewer.objects.bulk_create(reviewers)

    operations = [
        migrations.RunPython(seed_reviewers),
    ]
