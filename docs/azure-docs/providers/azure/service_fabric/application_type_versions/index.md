---
title: application_type_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - application_type_versions
  - service_fabric
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

Creates, updates, deletes, gets or lists a <code>application_type_versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application_type_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric.application_type_versions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_application_type_versions', value: 'view', },
        { label: 'application_type_versions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Azure resource identifier. |
| <CopyableCode code="name" /> | `text` | Azure resource name. |
| <CopyableCode code="app_package_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="applicationTypeName" /> | `text` | field from the `properties` object |
| <CopyableCode code="clusterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_parameter_list" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | Azure resource etag. |
| <CopyableCode code="location" /> | `text` | It will be deprecated in New API, resource location depends on the parent resource. |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Azure resource tags. |
| <CopyableCode code="type" /> | `text` | Azure resource type. |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Azure resource identifier. |
| <CopyableCode code="name" /> | `string` | Azure resource name. |
| <CopyableCode code="etag" /> | `string` | Azure resource etag. |
| <CopyableCode code="location" /> | `string` | It will be deprecated in New API, resource location depends on the parent resource. |
| <CopyableCode code="properties" /> | `object` | The properties of the application type version resource. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Azure resource tags. |
| <CopyableCode code="type" /> | `string` | Azure resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="applicationTypeName, clusterName, resourceGroupName, subscriptionId, version" /> | Get a Service Fabric application type version resource created or in the process of being created in the Service Fabric application type name resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="applicationTypeName, clusterName, resourceGroupName, subscriptionId" /> | Gets all application type version resources created or in the process of being created in the Service Fabric application type name resource. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="applicationTypeName, clusterName, resourceGroupName, subscriptionId, version" /> | Create or update a Service Fabric application type version resource with the specified name. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="applicationTypeName, clusterName, resourceGroupName, subscriptionId, version" /> | Delete a Service Fabric application type version resource with the specified name. |

## `SELECT` examples

Gets all application type version resources created or in the process of being created in the Service Fabric application type name resource.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_application_type_versions', value: 'view', },
        { label: 'application_type_versions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
app_package_url,
applicationTypeName,
clusterName,
default_parameter_list,
etag,
location,
provisioning_state,
resourceGroupName,
subscriptionId,
system_data,
tags,
type,
version
FROM azure.service_fabric.vw_application_type_versions
WHERE applicationTypeName = '{{ applicationTypeName }}'
AND clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
location,
properties,
systemData,
tags,
type
FROM azure.service_fabric.application_type_versions
WHERE applicationTypeName = '{{ applicationTypeName }}'
AND clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>application_type_versions</code> resource.

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
INSERT INTO azure.service_fabric.application_type_versions (
applicationTypeName,
clusterName,
resourceGroupName,
subscriptionId,
version,
properties,
location,
tags,
systemData
)
SELECT 
'{{ applicationTypeName }}',
'{{ clusterName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ version }}',
'{{ properties }}',
'{{ location }}',
'{{ tags }}',
'{{ systemData }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: provisioningState
          value: string
        - name: appPackageUrl
          value: string
        - name: defaultParameterList
          value: []
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: location
      value: string
    - name: tags
      value: object
    - name: etag
      value: string
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>application_type_versions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.service_fabric.application_type_versions
WHERE applicationTypeName = '{{ applicationTypeName }}'
AND clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND version = '{{ version }}';
```
