---
title: applications_by_ids
hide_title: false
hide_table_of_contents: false
keywords:
  - applications_by_ids
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

Creates, updates, deletes, gets or lists a <code>applications_by_ids</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>applications_by_ids</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_applications.applications_by_ids" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="applicationId, data__kind, data__properties" /> | Creates or updates a managed application. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>applications_by_ids</code> resource.

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
INSERT INTO azure.managed_applications.applications_by_ids (
applicationId,
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
'{{ applicationId }}',
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
