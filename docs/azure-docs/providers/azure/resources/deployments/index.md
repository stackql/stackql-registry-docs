---
title: deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments
  - resources
  - azure
  - microsoft azure
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Microsoft Azure infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>deployments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resources.deployments" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_deployments', value: 'view', },
        { label: 'deployments', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The ID of the deployment. |
| <CopyableCode code="name" /> | `text` | The name of the deployment. |
| <CopyableCode code="correlation_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="debug_setting" /> | `text` | field from the `properties` object |
| <CopyableCode code="dependencies" /> | `text` | field from the `properties` object |
| <CopyableCode code="deploymentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="duration" /> | `text` | field from the `properties` object |
| <CopyableCode code="error" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | the location of the deployment. |
| <CopyableCode code="mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="on_error_deployment" /> | `text` | field from the `properties` object |
| <CopyableCode code="output_resources" /> | `text` | field from the `properties` object |
| <CopyableCode code="outputs" /> | `text` | field from the `properties` object |
| <CopyableCode code="parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="parameters_link" /> | `text` | field from the `properties` object |
| <CopyableCode code="providers" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Deployment tags |
| <CopyableCode code="template_hash" /> | `text` | field from the `properties` object |
| <CopyableCode code="template_link" /> | `text` | field from the `properties` object |
| <CopyableCode code="timestamp" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the deployment. |
| <CopyableCode code="validated_resources" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the deployment. |
| <CopyableCode code="name" /> | `string` | The name of the deployment. |
| <CopyableCode code="location" /> | `string` | the location of the deployment. |
| <CopyableCode code="properties" /> | `object` | Deployment properties with additional details. |
| <CopyableCode code="tags" /> | `object` | Deployment tags |
| <CopyableCode code="type" /> | `string` | The type of the deployment. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deploymentName, resourceGroupName, subscriptionId" /> | Gets a deployment. |
| <CopyableCode code="get_at_management_group_scope" /> | `SELECT` | <CopyableCode code="deploymentName, groupId" /> | Gets a deployment. |
| <CopyableCode code="get_at_scope" /> | `SELECT` | <CopyableCode code="deploymentName, scope" /> | Gets a deployment. |
| <CopyableCode code="get_at_subscription_scope" /> | `SELECT` | <CopyableCode code="deploymentName, subscriptionId" /> | Gets a deployment. |
| <CopyableCode code="get_at_tenant_scope" /> | `SELECT` | <CopyableCode code="deploymentName" /> | Gets a deployment. |
| <CopyableCode code="list_at_management_group_scope" /> | `SELECT` | <CopyableCode code="groupId" /> | Get all the deployments for a management group. |
| <CopyableCode code="list_at_scope" /> | `SELECT` | <CopyableCode code="scope" /> | Get all the deployments at the given scope. |
| <CopyableCode code="list_at_subscription_scope" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get all the deployments for a subscription. |
| <CopyableCode code="list_at_tenant_scope" /> | `SELECT` | <CopyableCode code="" /> | Get all the deployments at the tenant scope. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get all the deployments for a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="deploymentName, resourceGroupName, subscriptionId, data__properties" /> | You can provide the template and parameters directly in the request or link to JSON files. |
| <CopyableCode code="create_or_update_at_management_group_scope" /> | `INSERT` | <CopyableCode code="deploymentName, groupId, data__location, data__properties" /> | You can provide the template and parameters directly in the request or link to JSON files. |
| <CopyableCode code="create_or_update_at_scope" /> | `INSERT` | <CopyableCode code="deploymentName, scope, data__properties" /> | You can provide the template and parameters directly in the request or link to JSON files. |
| <CopyableCode code="create_or_update_at_subscription_scope" /> | `INSERT` | <CopyableCode code="deploymentName, subscriptionId, data__properties" /> | You can provide the template and parameters directly in the request or link to JSON files. |
| <CopyableCode code="create_or_update_at_tenant_scope" /> | `INSERT` | <CopyableCode code="deploymentName, data__location, data__properties" /> | You can provide the template and parameters directly in the request or link to JSON files. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="deploymentName, resourceGroupName, subscriptionId" /> | A template deployment that is currently running cannot be deleted. Deleting a template deployment removes the associated deployment operations. Deleting a template deployment does not affect the state of the resource group. This is an asynchronous operation that returns a status of 202 until the template deployment is successfully deleted. The Location response header contains the URI that is used to obtain the status of the process. While the process is running, a call to the URI in the Location header returns a status of 202. When the process finishes, the URI in the Location header returns a status of 204 on success. If the asynchronous request failed, the URI in the Location header returns an error-level status code. |
| <CopyableCode code="calculate_template_hash" /> | `EXEC` | <CopyableCode code="" /> | Calculate the hash of the given template. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="deploymentName, resourceGroupName, subscriptionId" /> | You can cancel a deployment only if the provisioningState is Accepted or Running. After the deployment is canceled, the provisioningState is set to Canceled. Canceling a template deployment stops the currently running template deployment and leaves the resource group partially deployed. |
| <CopyableCode code="cancel_at_management_group_scope" /> | `EXEC` | <CopyableCode code="deploymentName, groupId" /> | You can cancel a deployment only if the provisioningState is Accepted or Running. After the deployment is canceled, the provisioningState is set to Canceled. Canceling a template deployment stops the currently running template deployment and leaves the resources partially deployed. |
| <CopyableCode code="cancel_at_scope" /> | `EXEC` | <CopyableCode code="deploymentName, scope" /> | You can cancel a deployment only if the provisioningState is Accepted or Running. After the deployment is canceled, the provisioningState is set to Canceled. Canceling a template deployment stops the currently running template deployment and leaves the resources partially deployed. |
| <CopyableCode code="cancel_at_subscription_scope" /> | `EXEC` | <CopyableCode code="deploymentName, subscriptionId" /> | You can cancel a deployment only if the provisioningState is Accepted or Running. After the deployment is canceled, the provisioningState is set to Canceled. Canceling a template deployment stops the currently running template deployment and leaves the resources partially deployed. |
| <CopyableCode code="cancel_at_tenant_scope" /> | `EXEC` | <CopyableCode code="deploymentName" /> | You can cancel a deployment only if the provisioningState is Accepted or Running. After the deployment is canceled, the provisioningState is set to Canceled. Canceling a template deployment stops the currently running template deployment and leaves the resources partially deployed. |
| <CopyableCode code="delete_at_management_group_scope" /> | `EXEC` | <CopyableCode code="deploymentName, groupId" /> | A template deployment that is currently running cannot be deleted. Deleting a template deployment removes the associated deployment operations. This is an asynchronous operation that returns a status of 202 until the template deployment is successfully deleted. The Location response header contains the URI that is used to obtain the status of the process. While the process is running, a call to the URI in the Location header returns a status of 202. When the process finishes, the URI in the Location header returns a status of 204 on success. If the asynchronous request failed, the URI in the Location header returns an error-level status code. |
| <CopyableCode code="delete_at_scope" /> | `EXEC` | <CopyableCode code="deploymentName, scope" /> | A template deployment that is currently running cannot be deleted. Deleting a template deployment removes the associated deployment operations. This is an asynchronous operation that returns a status of 202 until the template deployment is successfully deleted. The Location response header contains the URI that is used to obtain the status of the process. While the process is running, a call to the URI in the Location header returns a status of 202. When the process finishes, the URI in the Location header returns a status of 204 on success. If the asynchronous request failed, the URI in the Location header returns an error-level status code. |
| <CopyableCode code="delete_at_subscription_scope" /> | `EXEC` | <CopyableCode code="deploymentName, subscriptionId" /> | A template deployment that is currently running cannot be deleted. Deleting a template deployment removes the associated deployment operations. This is an asynchronous operation that returns a status of 202 until the template deployment is successfully deleted. The Location response header contains the URI that is used to obtain the status of the process. While the process is running, a call to the URI in the Location header returns a status of 202. When the process finishes, the URI in the Location header returns a status of 204 on success. If the asynchronous request failed, the URI in the Location header returns an error-level status code. |
| <CopyableCode code="delete_at_tenant_scope" /> | `EXEC` | <CopyableCode code="deploymentName" /> | A template deployment that is currently running cannot be deleted. Deleting a template deployment removes the associated deployment operations. This is an asynchronous operation that returns a status of 202 until the template deployment is successfully deleted. The Location response header contains the URI that is used to obtain the status of the process. While the process is running, a call to the URI in the Location header returns a status of 202. When the process finishes, the URI in the Location header returns a status of 204 on success. If the asynchronous request failed, the URI in the Location header returns an error-level status code. |
| <CopyableCode code="export_template" /> | `EXEC` | <CopyableCode code="deploymentName, resourceGroupName, subscriptionId" /> | Exports the template used for specified deployment. |
| <CopyableCode code="export_template_at_management_group_scope" /> | `EXEC` | <CopyableCode code="deploymentName, groupId" /> | Exports the template used for specified deployment. |
| <CopyableCode code="export_template_at_scope" /> | `EXEC` | <CopyableCode code="deploymentName, scope" /> | Exports the template used for specified deployment. |
| <CopyableCode code="export_template_at_subscription_scope" /> | `EXEC` | <CopyableCode code="deploymentName, subscriptionId" /> | Exports the template used for specified deployment. |
| <CopyableCode code="export_template_at_tenant_scope" /> | `EXEC` | <CopyableCode code="deploymentName" /> | Exports the template used for specified deployment. |
| <CopyableCode code="validate" /> | `EXEC` | <CopyableCode code="deploymentName, resourceGroupName, subscriptionId, data__properties" /> | Validates whether the specified template is syntactically correct and will be accepted by Azure Resource Manager.. |
| <CopyableCode code="validate_at_management_group_scope" /> | `EXEC` | <CopyableCode code="deploymentName, groupId, data__location, data__properties" /> | Validates whether the specified template is syntactically correct and will be accepted by Azure Resource Manager.. |
| <CopyableCode code="validate_at_scope" /> | `EXEC` | <CopyableCode code="deploymentName, scope, data__properties" /> | Validates whether the specified template is syntactically correct and will be accepted by Azure Resource Manager.. |
| <CopyableCode code="validate_at_subscription_scope" /> | `EXEC` | <CopyableCode code="deploymentName, subscriptionId, data__properties" /> | Validates whether the specified template is syntactically correct and will be accepted by Azure Resource Manager.. |
| <CopyableCode code="validate_at_tenant_scope" /> | `EXEC` | <CopyableCode code="deploymentName, data__location, data__properties" /> | Validates whether the specified template is syntactically correct and will be accepted by Azure Resource Manager.. |
| <CopyableCode code="what_if" /> | `EXEC` | <CopyableCode code="deploymentName, resourceGroupName, subscriptionId, data__properties" /> | Returns changes that will be made by the deployment if executed at the scope of the resource group. |
| <CopyableCode code="what_if_at_management_group_scope" /> | `EXEC` | <CopyableCode code="deploymentName, groupId, data__location, data__properties" /> | Returns changes that will be made by the deployment if executed at the scope of the management group. |
| <CopyableCode code="what_if_at_subscription_scope" /> | `EXEC` | <CopyableCode code="deploymentName, subscriptionId, data__properties" /> | Returns changes that will be made by the deployment if executed at the scope of the subscription. |
| <CopyableCode code="what_if_at_tenant_scope" /> | `EXEC` | <CopyableCode code="deploymentName, data__location, data__properties" /> | Returns changes that will be made by the deployment if executed at the scope of the tenant group. |

## `SELECT` examples

Get all the deployments at the tenant scope.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_deployments', value: 'view', },
        { label: 'deployments', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
correlation_id,
debug_setting,
dependencies,
deploymentName,
duration,
error,
location,
mode,
on_error_deployment,
output_resources,
outputs,
parameters,
parameters_link,
providers,
provisioning_state,
resourceGroupName,
subscriptionId,
tags,
template_hash,
template_link,
timestamp,
type,
validated_resources
FROM azure.resources.vw_deployments
;
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
FROM azure.resources.deployments
;
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>deployments</code> resource.

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
INSERT INTO azure.resources.deployments (
deploymentName,
scope,
data__properties,
location,
properties,
tags
)
SELECT 
'{{ deploymentName }}',
'{{ scope }}',
'{{ data__properties }}',
'{{ location }}',
'{{ properties }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: location
      value: string
    - name: properties
      value:
        - name: template
          value: object
        - name: templateLink
          value:
            - name: uri
              value: string
            - name: id
              value: string
            - name: relativePath
              value: string
            - name: contentVersion
              value: string
            - name: queryString
              value: string
        - name: parameters
          value: object
        - name: parametersLink
          value:
            - name: uri
              value: string
            - name: contentVersion
              value: string
        - name: mode
          value: string
        - name: debugSetting
          value:
            - name: detailLevel
              value: string
        - name: onErrorDeployment
          value:
            - name: type
              value: string
            - name: deploymentName
              value: string
        - name: expressionEvaluationOptions
          value:
            - name: scope
              value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>deployments</code> resource.

```sql
/*+ delete */
DELETE FROM azure.resources.deployments
WHERE deploymentName = '{{ deploymentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
