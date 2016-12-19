#Compares two words and outputs sentence counts for September 2016

import mediacloud, datetime
import logging



mc = mediacloud.api.MediaCloud('Insert_API_KEY_HERE')

def CompareCounts():
    
    input1 = raw_input("First Term: ")
    input2 = raw_input("Second Term: ")
    
    logging.basicConfig(filename='Error_Log.log',level=logging.INFO)
    logging.debug('Checking to see if the Media Cloud API was correctly called')

   # logging.info('succes', phrase1, phrase2)
    
    Count1 = mc.sentenceCount(input1, solr_filter=[mc.publish_date_query( datetime.date( 2016, 9, 1), datetime.date( 2016, 9, 30) ), 'tags_id_media:1' ])
    Count2 = mc.sentenceCount(input2, solr_filter=[mc.publish_date_query( datetime.date( 2016, 9, 1), datetime.date( 2016, 9, 30) ), 'tags_id_media:1' ])
    
	#tests to see if the api returns something
    if Count1['count'] < 1:
	    logging.warning('No Media Mentions for First Term')
		
    if Count2['count'] < 1:
	    logging.warning('No Media Mentions for Second Term')
	
    print Count1['count'] # prints the number of sentences found
    print Count2['count'] # prints the number of sentences found
    
    logging.info(Count1,Count2)

CompareCounts()