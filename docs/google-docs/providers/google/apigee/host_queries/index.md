---
title: host_queries
hide_title: false
hide_table_of_contents: false
keywords:
  - host_queries
  - apigee
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>host_queries</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>host_queries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.host_queries" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Asynchronous Query Name. |
| <CopyableCode code="created" /> | `string` | Creation time of the query. |
| <CopyableCode code="envgroupHostname" /> | `string` | Hostname is available only when query is executed at host level. |
| <CopyableCode code="error" /> | `string` | Error is set when query fails. |
| <CopyableCode code="executionTime" /> | `string` | ExecutionTime is available only after the query is completed. |
| <CopyableCode code="queryParams" /> | `object` |  |
| <CopyableCode code="reportDefinitionId" /> | `string` | Asynchronous Report ID. |
| <CopyableCode code="result" /> | `object` |  |
| <CopyableCode code="resultFileSize" /> | `string` | ResultFileSize is available only after the query is completed. |
| <CopyableCode code="resultRows" /> | `string` | ResultRows is available only after the query is completed. |
| <CopyableCode code="self" /> | `string` | Self link of the query. Example: `/organizations/myorg/environments/myenv/queries/9cfc0d85-0f30-46d6-ae6f-318d0cb961bd` or following format if query is running at host level: `/organizations/myorg/hostQueries/9cfc0d85-0f30-46d6-ae6f-318d0cb961bd` |
| <CopyableCode code="state" /> | `string` | Query state could be "enqueued", "running", "completed", "failed". |
| <CopyableCode code="updated" /> | `string` | Last updated timestamp for the query. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_host_queries_get" /> | `SELECT` | <CopyableCode code="hostQueriesId, organizationsId" /> | Get status of a query submitted at host level. If the query is still in progress, the `state` is set to "running" After the query has completed successfully, `state` is set to "completed" |
| <CopyableCode code="organizations_host_queries_list" /> | `SELECT` | <CopyableCode code="organizationsId" /> | Return a list of Asynchronous Queries at host level. |
| <CopyableCode code="organizations_host_queries_create" /> | `INSERT` | <CopyableCode code="organizationsId" /> | Submit a query at host level to be processed in the background. If the submission of the query succeeds, the API returns a 201 status and an ID that refer to the query. In addition to the HTTP status 201, the `state` of "enqueued" means that the request succeeded. |

## `SELECT` examples

Return a list of Asynchronous Queries at host level.

```sql
SELECT
name,
created,
envgroupHostname,
error,
executionTime,
queryParams,
reportDefinitionId,
result,
resultFileSize,
resultRows,
self,
state,
updated
FROM google.apigee.host_queries
WHERE organizationsId = '{{ organizationsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>host_queries</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.apigee.host_queries (
organizationsId,
dimensions,
limit,
csvDelimiter,
envgroupHostname,
filter,
outputFormat,
name,
timeRange,
metrics,
groupByTimeUnit,
reportDefinitionId
)
SELECT 
'{{ organizationsId }}',
'{{ dimensions }}',
'{{ limit }}',
'{{ csvDelimiter }}',
'{{ envgroupHostname }}',
'{{ filter }}',
'{{ outputFormat }}',
'{{ name }}',
'{{ timeRange }}',
'{{ metrics }}',
'{{ groupByTimeUnit }}',
'{{ reportDefinitionId }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: dimensions
        value: '{{ dimensions }}'
      - name: limit
        value: '{{ limit }}'
      - name: csvDelimiter
        value: '{{ csvDelimiter }}'
      - name: envgroupHostname
        value: '{{ envgroupHostname }}'
      - name: filter
        value: '{{ filter }}'
      - name: outputFormat
        value: '{{ outputFormat }}'
      - name: name
        value: '{{ name }}'
      - name: timeRange
        value: '{{ timeRange }}'
      - name: metrics
        value: '{{ metrics }}'
      - name: groupByTimeUnit
        value: '{{ groupByTimeUnit }}'
      - name: reportDefinitionId
        value: '{{ reportDefinitionId }}'

```
</TabItem>
</Tabs>
