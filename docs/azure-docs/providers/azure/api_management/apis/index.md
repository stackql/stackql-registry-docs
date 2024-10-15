---
title: apis
hide_title: false
hide_table_of_contents: false
keywords:
  - apis
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

Creates, updates, deletes, gets or lists a <code>apis</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>apis</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.apis" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_apis', value: 'view', },
        { label: 'apis', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="apiId" /> | `text` | field from the `properties` object |
| <CopyableCode code="api_revision" /> | `text` | field from the `properties` object |
| <CopyableCode code="api_revision_description" /> | `text` | field from the `properties` object |
| <CopyableCode code="api_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="api_version_description" /> | `text` | field from the `properties` object |
| <CopyableCode code="api_version_set" /> | `text` | field from the `properties` object |
| <CopyableCode code="api_version_set_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="authentication_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="contact" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_current" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_online" /> | `text` | field from the `properties` object |
| <CopyableCode code="license" /> | `text` | field from the `properties` object |
| <CopyableCode code="path" /> | `text` | field from the `properties` object |
| <CopyableCode code="protocols" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_api_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscription_key_parameter_names" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscription_required" /> | `text` | field from the `properties` object |
| <CopyableCode code="terms_of_service_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | API Entity Properties |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="apiId, resourceGroupName, serviceName, subscriptionId" /> | Gets the details of the API specified by its identifier. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Lists all APIs of the API Management service instance. |
| <CopyableCode code="list_by_tags" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Lists a collection of apis associated with tags. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="apiId, resourceGroupName, serviceName, subscriptionId" /> | Creates new or updates existing specified API of the API Management service instance. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, apiId, resourceGroupName, serviceName, subscriptionId" /> | Deletes the specified API of the API Management service instance. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="If-Match, apiId, resourceGroupName, serviceName, subscriptionId" /> | Updates the specified API of the API Management service instance. |

## `SELECT` examples

Lists all APIs of the API Management service instance.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_apis', value: 'view', },
        { label: 'apis', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
apiId,
api_revision,
api_revision_description,
api_version,
api_version_description,
api_version_set,
api_version_set_id,
authentication_settings,
contact,
display_name,
is_current,
is_online,
license,
path,
protocols,
provisioning_state,
resourceGroupName,
serviceName,
service_url,
source_api_id,
subscriptionId,
subscription_key_parameter_names,
subscription_required,
terms_of_service_url,
type
FROM azure.api_management.vw_apis
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.api_management.apis
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>apis</code> resource.

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
INSERT INTO azure.api_management.apis (
apiId,
resourceGroupName,
serviceName,
subscriptionId,
properties
)
SELECT 
'{{ apiId }}',
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
        - name: value
          value: string
        - name: format
          value: string
        - name: wsdlSelector
          value:
            - name: wsdlServiceName
              value: string
            - name: wsdlEndpointName
              value: string
        - name: apiType
          value: string
        - name: translateRequiredQueryParameters
          value: string
        - name: sourceApiId
          value: string
        - name: displayName
          value: string
        - name: serviceUrl
          value: string
        - name: path
          value: string
        - name: protocols
          value:
            - string
        - name: apiVersionSet
          value:
            - name: id
              value: string
            - name: name
              value: string
            - name: description
              value: string
            - name: versioningScheme
              value: string
            - name: versionQueryName
              value: string
            - name: versionHeaderName
              value: string
        - name: provisioningState
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>apis</code> resource.

```sql
/*+ update */
UPDATE azure.api_management.apis
SET 
properties = '{{ properties }}'
WHERE 
If-Match = '{{ If-Match }}'
AND apiId = '{{ apiId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>apis</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_management.apis
WHERE If-Match = '{{ If-Match }}'
AND apiId = '{{ apiId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
