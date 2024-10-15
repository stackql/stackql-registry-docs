---
title: open_id_connect_providers
hide_title: false
hide_table_of_contents: false
keywords:
  - open_id_connect_providers
  - api_management
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

Creates, updates, deletes, gets or lists a <code>open_id_connect_providers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>open_id_connect_providers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.open_id_connect_providers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_open_id_connect_providers', value: 'view', },
        { label: 'open_id_connect_providers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="client_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="client_secret" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="metadata_endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="opid" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="use_in_api_documentation" /> | `text` | field from the `properties` object |
| <CopyableCode code="use_in_test_console" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | OpenID Connect Providers Contract. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="opid, resourceGroupName, serviceName, subscriptionId" /> | Gets specific OpenID Connect Provider without secrets. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Lists of all the OpenId Connect Providers. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="opid, resourceGroupName, serviceName, subscriptionId" /> | Creates or updates the OpenID Connect Provider. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, opid, resourceGroupName, serviceName, subscriptionId" /> | Deletes specific OpenID Connect Provider of the API Management service instance. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="If-Match, opid, resourceGroupName, serviceName, subscriptionId" /> | Updates the specific OpenID Connect Provider. |

## `SELECT` examples

Lists of all the OpenId Connect Providers.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_open_id_connect_providers', value: 'view', },
        { label: 'open_id_connect_providers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
client_id,
client_secret,
display_name,
metadata_endpoint,
opid,
resourceGroupName,
serviceName,
subscriptionId,
use_in_api_documentation,
use_in_test_console
FROM azure.api_management.vw_open_id_connect_providers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.api_management.open_id_connect_providers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>open_id_connect_providers</code> resource.

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
INSERT INTO azure.api_management.open_id_connect_providers (
opid,
resourceGroupName,
serviceName,
subscriptionId,
properties
)
SELECT 
'{{ opid }}',
'{{ resourceGroupName }}',
'{{ serviceName }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: displayName
          value: string
        - name: description
          value: string
        - name: metadataEndpoint
          value: string
        - name: clientId
          value: string
        - name: clientSecret
          value: string
        - name: useInTestConsole
          value: boolean
        - name: useInApiDocumentation
          value: boolean

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>open_id_connect_providers</code> resource.

```sql
/*+ update */
UPDATE azure.api_management.open_id_connect_providers
SET 
properties = '{{ properties }}'
WHERE 
If-Match = '{{ If-Match }}'
AND opid = '{{ opid }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>open_id_connect_providers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_management.open_id_connect_providers
WHERE If-Match = '{{ If-Match }}'
AND opid = '{{ opid }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
