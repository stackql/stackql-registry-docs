---
title: role_assignments_by_enrollment_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - role_assignments_by_enrollment_accounts
  - billing
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

Creates, updates, deletes, gets or lists a <code>role_assignments_by_enrollment_accounts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>role_assignments_by_enrollment_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.role_assignments_by_enrollment_accounts" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="billingAccountName, billingRoleAssignmentName, enrollmentAccountName" /> | Create or update a billing role assignment. The operation is supported only for billing accounts with agreement type Enterprise Agreement. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>role_assignments_by_enrollment_accounts</code> resource.

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
INSERT INTO azure.billing.role_assignments_by_enrollment_accounts (
billingAccountName,
billingRoleAssignmentName,
enrollmentAccountName,
tags,
properties
)
SELECT 
'{{ billingAccountName }}',
'{{ billingRoleAssignmentName }}',
'{{ enrollmentAccountName }}',
'{{ tags }}',
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
    - name: properties
      value:
        - name: provisioningState
          value: string
        - name: createdOn
          value: string
        - name: createdByPrincipalTenantId
          value: string
        - name: createdByPrincipalId
          value: string
        - name: createdByPrincipalPuid
          value: string
        - name: createdByUserEmailAddress
          value: string
        - name: modifiedOn
          value: string
        - name: modifiedByPrincipalPuid
          value: string
        - name: modifiedByUserEmailAddress
          value: string
        - name: modifiedByPrincipalId
          value: string
        - name: modifiedByPrincipalTenantId
          value: string
        - name: principalPuid
          value: string
        - name: principalId
          value: string
        - name: principalTenantId
          value: string
        - name: roleDefinitionId
          value: string
        - name: scope
          value: string
        - name: userAuthenticationType
          value: string
        - name: userEmailAddress
          value: string
        - name: principalTenantName
          value: string
        - name: principalDisplayName
          value: string
        - name: principalType
          value: string
        - name: billingRequestId
          value: string
        - name: billingAccountId
          value: string
        - name: billingAccountDisplayName
          value: string
        - name: billingProfileId
          value: string
        - name: billingProfileDisplayName
          value: string
        - name: invoiceSectionId
          value: string
        - name: invoiceSectionDisplayName
          value: string
        - name: customerId
          value: string
        - name: customerDisplayName
          value: string

```
</TabItem>
</Tabs>
