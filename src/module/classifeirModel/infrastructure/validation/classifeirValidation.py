from donttrust import DontTrust, Schema, ValidationError

class ClassifeirValidation:
    def validate_image(self):
        return DontTrust(
            image=Schema().string().required()
        )