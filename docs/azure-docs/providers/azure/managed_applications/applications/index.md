---
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
  - managed_applications
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

Creates, updates, deletes, gets or lists a <code>applications</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_applications.applications" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_applications', value: 'view', },
        { label: 'applications', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="applicationId" /> | `text` | field from the `properties` object |
| <CopyableCode code="applicationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="application_definition_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="artifacts" /> | `text` | field from the `properties` object |
| <CopyableCode code="authorizations" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="customer_support" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Identity for the resource. |
| <CopyableCode code="jit_access_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | The kind of the managed application. Allowed values are MarketPlace and ServiceCatalog. |
| <CopyableCode code="managed_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="managed_resource_group_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="management_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="outputs" /> | `text` | field from the `properties` object |
| <CopyableCode code="parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="plan" /> | `text` | Plan for the managed application. |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="publisher_tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | SKU for the resource. |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="support_urls" /> | `text` | field from the `properties` object |
| <CopyableCode code="updated_by" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Identity for the resource. |
| <CopyableCode code="kind" /> | `string` | The kind of the managed application. Allowed values are MarketPlace and ServiceCatalog. |
| <CopyableCode code="managedBy" /> | `string` | ID of the resource that manages this resource. |
| <CopyableCode code="plan" /> | `object` | Plan for the managed application. |
| <CopyableCode code="properties" /> | `object` | The managed application properties. |
| <CopyableCode code="sku" /> | `object` | SKU for the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="applicationName, resourceGroupName, subscriptionId" /> | Gets the managed application. |
| <CopyableCode code="get_by_id" /> | `SELECT` | <CopyableCode code="applicationId" /> | Gets the managed application. |
| <CopyableCode code="list_allowed_upgrade_plans" /> | `SELECT` | <CopyableCode code="applicationName, resourceGroupName, subscriptionId" /> | List allowed upgrade plans for application. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the applications within a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the applications within a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="applicationName, resourceGroupName, subscriptionId, data__kind, data__properties" /> | Creates or updates a managed application. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="applicationName, resourceGroupName, subscriptionId" /> | Deletes the managed application. |
| <CopyableCode code="delete_by_id" /> | `DELETE` | <CopyableCode code="applicationId" /> | Deletes the managed application. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="applicationName, resourceGroupName, subscriptionId" /> | Updates an existing managed application. |
| <CopyableCode code="refresh_permissions" /> | `EXEC` | <CopyableCode code="applicationName, resourceGroupName, subscriptionId" /> | Refresh Permissions for application. |
| <CopyableCode code="update_by_id" /> | `EXEC` | <CopyableCode code="applicationId" /> | Updates an existing managed application. |

## `SELECT` examples

Gets the managed application.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_applications', value: 'view', },
        { label: 'applications', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
applicationId,
applicationName,
application_definition_id,
artifacts,
authorizations,
billing_details,
created_by,
customer_support,
identity,
jit_access_policy,
kind,
managed_by,
managed_resource_group_id,
management_mode,
outputs,
parameters,
plan,
provisioning_state,
publisher_tenant_id,
resourceGroupName,
sku,
subscriptionId,
support_urls,
updated_by
FROM azure.managed_applications.vw_applications
WHERE applicationId = '{{ applicationId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
kind,
managedBy,
plan,
properties,
sku
FROM azure.managed_applications.applications
WHERE applicationId = '{{ applicationId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>applications</code> resource.

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
INSERT INTO azure.managed_applications.applications (
applicationName,
resourceGroupName,
subscriptionId,
data__kind,
data__properties,
properties,
plan,
kind,
identity,
managedBy,
sku
)
SELECT 
'{{ applicationName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__kind }}',
'{{ data__properties }}',
'{{ properties }}',
'{{ plan }}',
'{{ kind }}',
'{{ identity }}',
'{{ managedBy }}',
'{{ sku }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: managedResourceGroupId
          value: string
        - name: applicationDefinitionId
          value: string
        - name: parameters
          value: object
        - name: outputs
          value: object
        - name: provisioningState
          value: []
        - name: billingDetails
          value:
            - name: resourceUsageId
              value: string
        - name: jitAccessPolicy
          value:
            - name: jitAccessEnabled
              value: boolean
            - name: jitApprovalMode
              value: []
            - name: jitApprovers
              value:
                - - name: id
                    value: string
                  - name: type
                    value: string
                  - name: displayName
                    value: string
            - name: maximumJitAccessDuration
              value: string
        - name: publisherTenantId
          value: string
        - name: authorizations
          value:
            - - name: principalId
                value: string
              - name: roleDefinitionId
                value: string
        - name: managementMode
          value: []
        - name: customerSupport
          value:
            - name: contactName
              value: string
            - name: email
              value: string
            - name: phone
              value: string
        - name: supportUrls
          value:
            - name: publicAzure
              value: string
            - name: governmentCloud
              value: string
        - name: artifacts
          value:
            - - name: name
                value: []
              - name: uri
                value: string
              - name: type
                value: []
        - name: createdBy
          value:
            - name: oid
              value: string
            - name: puid
              value: string
            - name: applicationId
              value: string
    - name: plan
      value:
        - name: name
          value: string
        - name: publisher
          value: string
        - name: product
          value: string
        - name: promotionCode
          value: string
        - name: version
          value: string
    - name: kind
      value: string
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: string
        - name: userAssignedIdentities
          value: object
    - name: managedBy
      value: string
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: string
        - name: size
          value: string
        - name: family
          value: string
        - name: model
          value: string
        - name: capacity
          value: integer

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>applications</code> resource.

```sql
/*+ update */
UPDATE azure.managed_applications.applications
SET 
properties = '{{ properties }}',
plan = '{{ plan }}',
kind = '{{ kind }}',
identity = '{{ identity }}',
managedBy = '{{ managedBy }}',
sku = '{{ sku }}'
WHERE 
applicationName = '{{ applicationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>applications</code> resource.

```sql
/*+ delete */
DELETE FROM azure.managed_applications.applications
WHERE applicationId = '{{ applicationId }}';
```
