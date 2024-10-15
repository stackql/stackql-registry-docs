---
title: custom_domains
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_domains
  - cdn
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

Creates, updates, deletes, gets or lists a <code>custom_domains</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.custom_domains" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_custom_domains', value: 'view', },
        { label: 'custom_domains', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="customDomainName" /> | `text` | field from the `properties` object |
| <CopyableCode code="custom_https_parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="custom_https_provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="custom_https_provisioning_substate" /> | `text` | field from the `properties` object |
| <CopyableCode code="endpointName" /> | `text` | field from the `properties` object |
| <CopyableCode code="host_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="profileName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="validation_data" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The JSON object that contains the properties of the custom domain to create. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="customDomainName, endpointName, profileName, resourceGroupName, subscriptionId" /> | Gets an existing custom domain within an endpoint. |
| <CopyableCode code="list_by_endpoint" /> | `SELECT` | <CopyableCode code="endpointName, profileName, resourceGroupName, subscriptionId" /> | Lists all of the existing custom domains within an endpoint. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="customDomainName, endpointName, profileName, resourceGroupName, subscriptionId" /> | Creates a new custom domain within an endpoint. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="customDomainName, endpointName, profileName, resourceGroupName, subscriptionId" /> | Deletes an existing custom domain within an endpoint. |
| <CopyableCode code="disable_custom_https" /> | `EXEC` | <CopyableCode code="customDomainName, endpointName, profileName, resourceGroupName, subscriptionId" /> | Disable https delivery of the custom domain. |
| <CopyableCode code="enable_custom_https" /> | `EXEC` | <CopyableCode code="customDomainName, endpointName, profileName, resourceGroupName, subscriptionId, data__certificateSource, data__protocolType" /> | Enable https delivery of the custom domain. |

## `SELECT` examples

Lists all of the existing custom domains within an endpoint.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_custom_domains', value: 'view', },
        { label: 'custom_domains', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
customDomainName,
custom_https_parameters,
custom_https_provisioning_state,
custom_https_provisioning_substate,
endpointName,
host_name,
profileName,
provisioning_state,
resourceGroupName,
resource_state,
subscriptionId,
validation_data
FROM azure.cdn.vw_custom_domains
WHERE endpointName = '{{ endpointName }}'
AND profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.cdn.custom_domains
WHERE endpointName = '{{ endpointName }}'
AND profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>custom_domains</code> resource.

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
INSERT INTO azure.cdn.custom_domains (
customDomainName,
endpointName,
profileName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ customDomainName }}',
'{{ endpointName }}',
'{{ profileName }}',
'{{ resourceGroupName }}',
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
        - name: hostName
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>custom_domains</code> resource.

```sql
/*+ delete */
DELETE FROM azure.cdn.custom_domains
WHERE customDomainName = '{{ customDomainName }}'
AND endpointName = '{{ endpointName }}'
AND profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
