# encoding: utf-8

"""
Picture shape.
"""

from pptx.constants import MSO
from pptx.shapes.shape import BaseShape


class Picture(BaseShape):
    """
    A picture shape, one that places an image on a slide. Corresponds to the
    ``<p:pic>`` element.
    """
    def __init__(self, pic, parent):
        super(Picture, self).__init__(pic, parent)
        self._pic = pic

    @property
    def left(self):
        """
        Distance between left edge of slide and left edge of this shape, in
        EMU.
        """
        return self._off.x

    @property
    def shape_type(self):
        """
        Unique integer identifying the type of this shape, unconditionally
        ``MSO.PICTURE`` in this case.
        """
        return MSO.PICTURE

    @property
    def top(self):
        """
        Distance between top of slide and top edge of this shape, in EMU.
        """
        return self._off.y

    @property
    def _off(self):
        """
        Get or add sp.spPr.xfrm.off element
        """
        spPr = self._pic.spPr
        xfrm = spPr.get_or_add_xfrm()
        return xfrm.get_or_add_off()
