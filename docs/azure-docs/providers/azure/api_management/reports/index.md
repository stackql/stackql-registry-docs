---
title: reports
hide_title: false
hide_table_of_contents: false
keywords:
  - reports
  - api_management
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>reports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.reports</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Name depending on report endpoint specifies product, API, operation or developer name. |
| `userId` | `string` | User identifier path. /users/&#123;userId&#125; |
| `callCountBlocked` | `integer` | Number of calls blocked due to invalid credentials. This includes calls returning HttpStatusCode.Unauthorized and HttpStatusCode.Forbidden and HttpStatusCode.TooManyRequests |
| `country` | `string` | Country to which this record data is related. |
| `serviceTimeMin` | `number` | Minimum time it took to process request on backend. |
| `apiTimeMax` | `number` | Maximum time it took to process request. |
| `callCountTotal` | `integer` | Total number of calls. |
| `subscriptionId` | `string` | Subscription identifier path. /subscriptions/&#123;subscriptionId&#125; |
| `apiTimeMin` | `number` | Minimum time it took to process request. |
| `cacheHitCount` | `integer` | Number of times when content was served from cache policy. |
| `callCountSuccess` | `integer` | Number of successful calls. This includes calls returning HttpStatusCode &lt;= 301 and HttpStatusCode.NotModified and HttpStatusCode.TemporaryRedirect |
| `productId` | `string` | Product identifier path. /products/&#123;productId&#125; |
| `zip` | `string` | Zip code to which this record data is related. |
| `serviceTimeMax` | `number` | Maximum time it took to process request on backend. |
| `operationId` | `string` | Operation identifier path. /apis/&#123;apiId&#125;/operations/&#123;operationId&#125; |
| `apiId` | `string` | API identifier path. /apis/&#123;apiId&#125; |
| `apiRegion` | `string` | API region identifier. |
| `callCountFailed` | `integer` | Number of calls failed due to proxy or backend errors. This includes calls returning HttpStatusCode.BadRequest(400) and any Code between HttpStatusCode.InternalServerError (500) and 600 |
| `serviceTimeAvg` | `number` | Average time it took to process request on backend. |
| `cacheMissCount` | `integer` | Number of times content was fetched from backend. |
| `bandwidth` | `integer` | Bandwidth consumed. |
| `apiTimeAvg` | `number` | Average time it took to process request. |
| `timestamp` | `string` | Start of aggregation period. The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.<br /> |
| `region` | `string` | Country region to which this record data is related. |
| `callCountOther` | `integer` | Number of other calls. |
| `interval` | `string` | Length of aggregation period.  Interval must be multiple of 15 minutes and may not be zero. The value should be in ISO 8601 format (http://en.wikipedia.org/wiki/ISO_8601#Durations). |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Reports_ListBySubscription` | `SELECT` | `$filter, resourceGroupName, serviceName, subscriptionId` | Lists report records by subscription. |
| `Reports_ListByApi` | `EXEC` | `$filter, resourceGroupName, serviceName, subscriptionId` | Lists report records by API. |
| `Reports_ListByGeo` | `EXEC` | `$filter, resourceGroupName, serviceName, subscriptionId` | Lists report records by geography. |
| `Reports_ListByOperation` | `EXEC` | `$filter, resourceGroupName, serviceName, subscriptionId` | Lists report records by API Operations. |
| `Reports_ListByProduct` | `EXEC` | `$filter, resourceGroupName, serviceName, subscriptionId` | Lists report records by Product. |
| `Reports_ListByRequest` | `EXEC` | `$filter, resourceGroupName, serviceName, subscriptionId` | Lists report records by Request. |
| `Reports_ListByTime` | `EXEC` | `$filter, interval, resourceGroupName, serviceName, subscriptionId` | Lists report records by Time. |
| `Reports_ListByUser` | `EXEC` | `$filter, resourceGroupName, serviceName, subscriptionId` | Lists report records by User. |
