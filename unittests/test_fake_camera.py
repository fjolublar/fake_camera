from fake_camera import FakeCamera  # import the class


def test_fake_camera():
    fake_cam_object = FakeCamera().add_foreground_image("/workspaces/fake_camera/unittests/lena_color.jpg").add_background_image().build()
    _ = fake_cam_object.get_snapshot()
