class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        #flip
        for row in image:
            j = len(row)-1
            for i in range(len(row)//2):
                row[i], row[j-i] = row[j-i], row[i]
        #inverse
        for row in image:
            for k in range(len(row)):
                row[k] = int(not bool(row[k]))
        return image
