---
title: security_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - security_policies
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

Creates, updates, deletes, gets or lists a <code>security_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.security_policies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_security_policies', value: 'view', },
        { label: 'security_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="deployment_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="profileName" /> | `text` | field from the `properties` object |
| <CopyableCode code="profile_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="securityPolicyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The json object that contains properties required to create a security policy |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="profileName, resourceGroupName, securityPolicyName, subscriptionId" /> | Gets an existing security policy within a profile. |
| <CopyableCode code="list_by_profile" /> | `SELECT` | <CopyableCode code="profileName, resourceGroupName, subscriptionId" /> | Lists security policies associated with the profile |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="profileName, resourceGroupName, securityPolicyName, subscriptionId" /> | Creates a new security policy within the specified profile. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="profileName, resourceGroupName, securityPolicyName, subscriptionId" /> | Deletes an existing security policy within profile. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="profileName, resourceGroupName, securityPolicyName, subscriptionId" /> | Updates an existing security policy within a profile. |

## `SELECT` examples

Lists security policies associated with the profile

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_security_policies', value: 'view', },
        { label: 'security_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
deployment_status,
parameters,
profileName,
profile_name,
provisioning_state,
resourceGroupName,
securityPolicyName,
subscriptionId
FROM azure.cdn.vw_security_policies
WHERE profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.cdn.security_policies
WHERE profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>security_policies</code> resource.

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
INSERT INTO azure.cdn.security_policies (
profileName,
resourceGroupName,
securityPolicyName,
subscriptionId,
properties
)
SELECT 
'{{ profileName }}',
'{{ resourceGroupName }}',
'{{ securityPolicyName }}',
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
        - name: provisioningState
          value: string
        - name: deploymentStatus
          value: string
        - name: profileName
          value: string
        - name: parameters
          value:
            - name: type
              value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>security_policies</code> resource.

```sql
/*+ update */
UPDATE azure.cdn.security_policies
SET 
properties = '{{ properties }}'
WHERE 
profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND securityPolicyName = '{{ securityPolicyName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>security_policies</code> resource.

```sql
/*+ delete */
DELETE FROM azure.cdn.security_policies
WHERE profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND securityPolicyName = '{{ securityPolicyName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
