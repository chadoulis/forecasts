from django import template
register=template.Library()


@register.simple_tag
def Pagination(baseUrl,currentPage,totalPages,currentPageRadius):
	data=[1]
	num=currentPageRadius
	for i in range(currentPageRadius):
		toAppend=currentPage-num
		if toAppend>1:
			data.append(toAppend)
		num-=1
	if currentPage>1 and currentPage<totalPages:
		data.append(currentPage)
	for i in range(currentPageRadius):
		toAppend=currentPage+i+1
		if toAppend<totalPages:
			data.append(toAppend)
	if totalPages!=1:
		data.append(totalPages)
	ob=''
	for pageNumer in data:
		css=' firstLast'if pageNumer==1 or pageNumer==totalPages else''
		css+=' selected'if pageNumer==currentPage else''
		ob+='<a class="paginationElement spx10 spy10'+css+'" href="'+baseUrl+('/'+str(pageNumer) if pageNumer>1 else'')+'">'+str(pageNumer)+'</a>'
	return ob


componentIndexData={}
@register.simple_tag
def ComponentIndex(componentName,startWith=0):
	global componentIndexData
	try:
		componentIndexData[componentName]
	except:
		componentIndexData[componentName]=startWith-1
	componentIndexData[componentName]+=1
	return componentIndexData[componentName]
