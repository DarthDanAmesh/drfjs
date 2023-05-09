from django.contrib.auth import get_user_model

from rest_framework.serializers import ModelSerializer

User = get_user_model()


class UserUploadSerializer(ModelSerializer):
    class Meta:
        model = User
        """
        # add any to the fields for more json body response
         "middle_name", "first_two_names", "id_number",
                                 "email",  "resume", "cover", "contact", "location"
        """
        # maps with javascript side so that bio = input1.files[0], contact = input1.files[0]
        fields = ["middle_name", "first_two_names", "email", "cover", "resume", "id_number", "contact", "location"]

    def save(self, *args, **kwargs):
        if self.instance.resume:
            self.instance.resume.delete()
        return super().save(*args, **kwargs)
