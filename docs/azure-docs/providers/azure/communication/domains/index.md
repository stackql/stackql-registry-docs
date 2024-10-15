---
title: domains
hide_title: false
hide_table_of_contents: false
keywords:
  - domains
  - communication
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

Creates, updates, deletes, gets or lists a <code>domains</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.communication.domains" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_domains', value: 'view', },
        { label: 'domains', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="data_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="domainName" /> | `text` | field from the `properties` object |
| <CopyableCode code="domain_management" /> | `text` | field from the `properties` object |
| <CopyableCode code="emailServiceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="from_sender_domain" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="mail_from_sender_domain" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="user_engagement_tracking" /> | `text` | field from the `properties` object |
| <CopyableCode code="verification_records" /> | `text` | field from the `properties` object |
| <CopyableCode code="verification_states" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | A class that describes the properties of a Domains resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="domainName, emailServiceName, resourceGroupName, subscriptionId" /> | Get the Domains resource and its properties. |
| <CopyableCode code="list_by_email_service_resource" /> | `SELECT` | <CopyableCode code="emailServiceName, resourceGroupName, subscriptionId" /> | Handles requests to list all Domains resources under the parent EmailServices resource. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="domainName, emailServiceName, resourceGroupName, subscriptionId" /> | Add a new Domains resource under the parent EmailService resource or update an existing Domains resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="domainName, emailServiceName, resourceGroupName, subscriptionId" /> | Operation to delete a Domains resource. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="domainName, emailServiceName, resourceGroupName, subscriptionId" /> | Operation to update an existing Domains resource. |
| <CopyableCode code="cancel_verification" /> | `EXEC` | <CopyableCode code="domainName, emailServiceName, resourceGroupName, subscriptionId, data__verificationType" /> | Cancel verification of DNS record. |
| <CopyableCode code="initiate_verification" /> | `EXEC` | <CopyableCode code="domainName, emailServiceName, resourceGroupName, subscriptionId, data__verificationType" /> | Initiate verification of DNS record. |

## `SELECT` examples

Handles requests to list all Domains resources under the parent EmailServices resource.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_domains', value: 'view', },
        { label: 'domains', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
data_location,
domainName,
domain_management,
emailServiceName,
from_sender_domain,
location,
mail_from_sender_domain,
provisioning_state,
resourceGroupName,
subscriptionId,
tags,
user_engagement_tracking,
verification_records,
verification_states
FROM azure.communication.vw_domains
WHERE emailServiceName = '{{ emailServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.communication.domains
WHERE emailServiceName = '{{ emailServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>domains</code> resource.

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
INSERT INTO azure.communication.domains (
domainName,
emailServiceName,
resourceGroupName,
subscriptionId,
tags,
location,
properties
)
SELECT 
'{{ domainName }}',
'{{ emailServiceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ tags }}',
'{{ location }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: tags
      value: object
    - name: location
      value: string
    - name: properties
      value:
        - name: provisioningState
          value: string
        - name: dataLocation
          value: string
        - name: fromSenderDomain
          value: string
        - name: mailFromSenderDomain
          value: string
        - name: domainManagement
          value: []
        - name: verificationStates
          value:
            - name: Domain
              value:
                - name: status
                  value: string
                - name: errorCode
                  value: string
        - name: verificationRecords
          value:
            - name: Domain
              value:
                - name: type
                  value: string
                - name: name
                  value: string
                - name: value
                  value: string
                - name: ttl
                  value: integer
        - name: userEngagementTracking
          value: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>domains</code> resource.

```sql
/*+ update */
UPDATE azure.communication.domains
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
domainName = '{{ domainName }}'
AND emailServiceName = '{{ emailServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>domains</code> resource.

```sql
/*+ delete */
DELETE FROM azure.communication.domains
WHERE domainName = '{{ domainName }}'
AND emailServiceName = '{{ emailServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
