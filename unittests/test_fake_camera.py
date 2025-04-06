from fake_camera import FakeCamera  # import the class


def test_fake_camera():
    fake_cam_object = FakeCamera("./lena_color.jpg").add_foreground_image().add_background_image().build()
    snapshot = fake_cam_object.get_snapshot()
    assert snapshot
