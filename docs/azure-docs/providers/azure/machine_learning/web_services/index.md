---
title: web_services
hide_title: false
hide_table_of_contents: false
keywords:
  - web_services
  - machine_learning
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

Creates, updates, deletes, gets or lists a <code>web_services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>web_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.machine_learning.web_services" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_web_services', value: 'view', },
        { label: 'web_services', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Specifies the resource ID. |
| <CopyableCode code="name" /> | `text` | Specifies the name of the resource. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="assets" /> | `text` | field from the `properties` object |
| <CopyableCode code="commitment_plan" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_on" /> | `text` | field from the `properties` object |
| <CopyableCode code="diagnostics" /> | `text` | field from the `properties` object |
| <CopyableCode code="example_request" /> | `text` | field from the `properties` object |
| <CopyableCode code="expose_sample_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="input" /> | `text` | field from the `properties` object |
| <CopyableCode code="keys" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Specifies the location of the resource. |
| <CopyableCode code="machine_learning_workspace" /> | `text` | field from the `properties` object |
| <CopyableCode code="modified_on" /> | `text` | field from the `properties` object |
| <CopyableCode code="output" /> | `text` | field from the `properties` object |
| <CopyableCode code="package_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="payloads_in_blob_storage" /> | `text` | field from the `properties` object |
| <CopyableCode code="payloads_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="read_only" /> | `text` | field from the `properties` object |
| <CopyableCode code="realtime_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_account" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="swagger_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Contains resource tags defined as key/value pairs. |
| <CopyableCode code="title" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Specifies the type of the resource. |
| <CopyableCode code="webServiceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Specifies the resource ID. |
| <CopyableCode code="name" /> | `string` | Specifies the name of the resource. |
| <CopyableCode code="location" /> | `string` | Specifies the location of the resource. |
| <CopyableCode code="properties" /> | `object` | The set of properties specific to the Azure ML web service resource. |
| <CopyableCode code="tags" /> | `object` | Contains resource tags defined as key/value pairs. |
| <CopyableCode code="type" /> | `string` | Specifies the type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, webServiceName" /> | Gets the Web Service Definition as specified by a subscription, resource group, and name. Note that the storage credentials and web service keys are not returned by this call. To get the web service access keys, call List Keys. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets the web services in the specified resource group. |
| <CopyableCode code="list_by_subscription_id" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets the web services in the specified subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, webServiceName, data__properties" /> | Create or update a web service. This call will overwrite an existing web service. Note that there is no warning or confirmation. This is a nonrecoverable operation. If your intent is to create a new web service, call the Get operation first to verify that it does not exist. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="resourceGroupName, subscriptionId, webServiceName" /> | Modifies an existing web service resource. The PATCH API call is an asynchronous operation. To determine whether it has completed successfully, you must perform a Get operation. |
| <CopyableCode code="remove" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, webServiceName" /> | Deletes the specified web service. |

## `SELECT` examples

Gets the web services in the specified subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_web_services', value: 'view', },
        { label: 'web_services', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
assets,
commitment_plan,
created_on,
diagnostics,
example_request,
expose_sample_data,
input,
keys,
location,
machine_learning_workspace,
modified_on,
output,
package_type,
parameters,
payloads_in_blob_storage,
payloads_location,
provisioning_state,
read_only,
realtime_configuration,
resourceGroupName,
storage_account,
subscriptionId,
swagger_location,
tags,
title,
type,
webServiceName
FROM azure.machine_learning.vw_web_services
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
tags,
type
FROM azure.machine_learning.web_services
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>web_services</code> resource.

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
INSERT INTO azure.machine_learning.web_services (
resourceGroupName,
subscriptionId,
webServiceName,
data__properties,
location,
tags,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ webServiceName }}',
'{{ data__properties }}',
'{{ location }}',
'{{ tags }}',
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
    - name: location
      value: string
    - name: type
      value: string
    - name: tags
      value: object
    - name: properties
      value:
        - name: title
          value: string
        - name: description
          value: string
        - name: createdOn
          value: string
        - name: modifiedOn
          value: string
        - name: provisioningState
          value: string
        - name: keys
          value:
            - name: primary
              value: string
            - name: secondary
              value: string
        - name: readOnly
          value: boolean
        - name: swaggerLocation
          value: string
        - name: exposeSampleData
          value: boolean
        - name: realtimeConfiguration
          value:
            - name: maxConcurrentCalls
              value: integer
        - name: diagnostics
          value:
            - name: level
              value: string
            - name: expiry
              value: string
        - name: storageAccount
          value:
            - name: name
              value: string
            - name: key
              value: string
        - name: machineLearningWorkspace
          value:
            - name: id
              value: string
        - name: commitmentPlan
          value:
            - name: id
              value: string
        - name: input
          value:
            - name: title
              value: string
            - name: description
              value: string
            - name: type
              value: string
            - name: properties
              value: object
        - name: exampleRequest
          value:
            - name: inputs
              value: object
            - name: globalParameters
              value: object
        - name: assets
          value: object
        - name: parameters
          value: object
        - name: packageType
          value: string
        - name: payloadsInBlobStorage
          value: boolean
        - name: payloadsLocation
          value:
            - name: uri
              value: string
            - name: credentials
              value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>web_services</code> resource.

```sql
/*+ update */
UPDATE azure.machine_learning.web_services
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND webServiceName = '{{ webServiceName }}';
```
