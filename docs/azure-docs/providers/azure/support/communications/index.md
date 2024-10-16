---
title: communications
hide_title: false
hide_table_of_contents: false
keywords:
  - communications
  - support
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

Creates, updates, deletes, gets or lists a <code>communications</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>communications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.support.communications" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_communications', value: 'view', },
        { label: 'communications', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Id of the resource. |
| <CopyableCode code="name" /> | `text` | Name of the resource. |
| <CopyableCode code="body" /> | `text` | field from the `properties` object |
| <CopyableCode code="communicationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="communication_direction" /> | `text` | field from the `properties` object |
| <CopyableCode code="communication_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="sender" /> | `text` | field from the `properties` object |
| <CopyableCode code="subject" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="supportTicketName" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Type of the resource 'Microsoft.Support/communications'. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Id of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a communication resource. |
| <CopyableCode code="type" /> | `string` | Type of the resource 'Microsoft.Support/communications'. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="communicationName, subscriptionId, supportTicketName" /> | Returns communication details for a support ticket. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId, supportTicketName" /> | Lists all communications (attachments not included) for a support ticket.  </br> You can also filter support ticket communications by _CreatedDate_ or _CommunicationType_ using the $filter parameter. The only type of communication supported today is _Web_. Output will be a paged result with _nextLink_, using which you can retrieve the next set of Communication results.   Support ticket data is available for 18 months after ticket creation. If a ticket was created more than 18 months ago, a request for data might cause an error. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="communicationName, subscriptionId, supportTicketName" /> | Adds a new customer communication to an Azure support ticket. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="subscriptionId, supportTicketName, data__name, data__type" /> | Check the availability of a resource name. This API should be used to check the uniqueness of the name for adding a new communication to the support ticket. |

## `SELECT` examples

Lists all communications (attachments not included) for a support ticket. <br/></br> You can also filter support ticket communications by _CreatedDate_ or _CommunicationType_ using the $filter parameter. The only type of communication supported today is _Web_. Output will be a paged result with _nextLink_, using which you can retrieve the next set of Communication results. <br/><br/>Support ticket data is available for 18 months after ticket creation. If a ticket was created more than 18 months ago, a request for data might cause an error.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_communications', value: 'view', },
        { label: 'communications', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
body,
communicationName,
communication_direction,
communication_type,
created_date,
sender,
subject,
subscriptionId,
supportTicketName,
type
FROM azure.support.vw_communications
WHERE subscriptionId = '{{ subscriptionId }}'
AND supportTicketName = '{{ supportTicketName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.support.communications
WHERE subscriptionId = '{{ subscriptionId }}'
AND supportTicketName = '{{ supportTicketName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>communications</code> resource.

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
INSERT INTO azure.support.communications (
communicationName,
subscriptionId,
supportTicketName,
properties
)
SELECT 
'{{ communicationName }}',
'{{ subscriptionId }}',
'{{ supportTicketName }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: properties
      value:
        - name: communicationType
          value: string
        - name: communicationDirection
          value: string
        - name: sender
          value: string
        - name: subject
          value: string
        - name: body
          value: string
        - name: createdDate
          value: string

```
</TabItem>
</Tabs>
