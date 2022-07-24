from tortoise import fields, Model


class AbstractBaseModel(Model):
    id = fields.IntField(pk=True)

    class Meta:
        abstract = True


class TgUser(AbstractBaseModel):
    tg_id = fields.IntField()


class GitlabEvent(AbstractBaseModel):
    pass
