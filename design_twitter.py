class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.feedL = []
        self.followL = []
        

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.feedL.append([userId, tweetId])
        
    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        L = []
        FL = self.getFollowees(userId)
        for i in self.feedL:
            if i[0] == userId or i[0] in FL :
                L.append(i[1])
        L.reverse()
        return L[:10]
    
    def getFollowees(self, userId):
        """
        Retrieve the followees user follows. 
        :type userId: int
        :rtype: List[int]
        """
        FL = []
        for i in self.followL:
            if i[0] == userId:
                FL.append(i[1])
        return FL

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if [followerId, followeeId] not in self.followL:
            self.followL.append([followerId, followeeId])
        

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if [followerId, followeeId] in self.followL:
            self.followL.remove([followerId, followeeId])

tw = Twitter()
tw.postTweet(1, 5) 
tw.postTweet(2, 3) 
print(tw.getNewsFeed(1))
tw.follow(1, 2)
print(tw.getNewsFeed(1))
tw.postTweet(2, 6)
print(tw.getNewsFeed(1))
tw.unfollow(1, 2)
print(tw.getNewsFeed(1))