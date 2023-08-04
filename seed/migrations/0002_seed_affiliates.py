from django.db import migrations

class Migration(migrations.Migration):
    
    dependencies = [
        ('seed', '0001_seed_reviewers'),
    ]

    def seed_affiliates(apps, schema_editor):
        Affiliate = apps.get_model('missions', 'Affiliate')
        affiliates = [
            Affiliate(affiliation="Planetary Science Institute"),
            Affiliate(affiliation="Planetary Data System"),
            Affiliate(affiliation="NASA Jet Propulsion Laboratory"),
            Affiliate(affiliation="California Institute of Technology"),
            Affiliate(affiliation="Johns Hopkins University Applied Physics Laboratory"),
            Affiliate(affiliation="Massachusetts Institute of Technology"),
            Affiliate(affiliation="University of Arizona"),
            Affiliate(affiliation="University of California, Berkeley"),
            Affiliate(affiliation="Cornell University"),
            Affiliate(affiliation="University of Colorado Boulder"),
            Affiliate(affiliation="University of Hawaii at Manoa"),
            Affiliate(affiliation="University of Michigan"),
            Affiliate(affiliation="University of Texas at Austin"),
            Affiliate(affiliation="University of Washington"),
            Affiliate(affiliation="University of California, Los Angeles"),
            Affiliate(affiliation="Georgia Institute of Technology"),
            Affiliate(affiliation="University of Illinois at Urbana-Champaign"),
            Affiliate(affiliation="University of Maryland"),
            Affiliate(affiliation="University of Chicago"),
            Affiliate(affiliation="Arizona State University"),
            Affiliate(affiliation="University of California, San Diego"),
            Affiliate(affiliation="Brown University"),
            Affiliate(affiliation="Harvard-Smithsonian Center for Astrophysics"),
            Affiliate(affiliation="University of California, Santa Cruz"),
            Affiliate(affiliation="University of Minnesota"),
            Affiliate(affiliation="University of Wisconsin-Madison"),
            Affiliate(affiliation="Texas A&M University")
        ]
        Affiliate.objects.bulk_create(affiliates)

    operations = [
        migrations.RunPython(seed_affiliates),
    ]