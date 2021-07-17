class Tasdasdasdasdasdasdasdasd:
    success = False
    failed = True
    warning = True
    another_param = False

    def _post_comment(self):
        """Example of complex function for flake8 to fail on.

        Has a complexity of 14 (number of branching paths)
        """
        if self.another_param:
            if self.success:
                if self.warning:
                    comment = "Build had issues"
                elif self.failed:
                    comment = "Build failed"
                else:
                    comment = "def"
            elif self.warning:
                if self.failed:
                    comment = "Build failed 2"
                else:
                    comment = "def2"
            else:
                comment = ":)"
        else:
            comment = "down there is too complex"
            # if you copy the above if body down here you will get a complexity of 14

        print(comment)
        if self.success:
            print("success")
        else:
            print("error")
