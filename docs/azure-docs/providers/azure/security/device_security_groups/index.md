---
title: device_security_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - device_security_groups
  - security
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

Creates, updates, deletes, gets or lists a <code>device_security_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>device_security_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.device_security_groups" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_device_security_groups', value: 'view', },
        { label: 'device_security_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="allowlist_rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="denylist_rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="deviceSecurityGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceId" /> | `text` | field from the `properties` object |
| <CopyableCode code="threshold_rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_window_rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="properties" /> | `object` | describes properties of a security group. |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deviceSecurityGroupName, resourceId" /> | Use this method to get the device security group for the specified IoT Hub resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceId" /> | Use this method get the list of device security groups for the specified IoT Hub resource. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="deviceSecurityGroupName, resourceId" /> | Use this method to creates or updates the device security group on a specified IoT Hub resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="deviceSecurityGroupName, resourceId" /> | User this method to deletes the device security group. |

## `SELECT` examples

Use this method get the list of device security groups for the specified IoT Hub resource.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_device_security_groups', value: 'view', },
        { label: 'device_security_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
allowlist_rules,
denylist_rules,
deviceSecurityGroupName,
resourceId,
threshold_rules,
time_window_rules,
type
FROM azure.security.vw_device_security_groups
WHERE resourceId = '{{ resourceId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.security.device_security_groups
WHERE resourceId = '{{ resourceId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>device_security_groups</code> resource.

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
INSERT INTO azure.security.device_security_groups (
deviceSecurityGroupName,
resourceId,
properties
)
SELECT 
'{{ deviceSecurityGroupName }}',
'{{ resourceId }}',
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
        - name: thresholdRules
          value:
            - - name: displayName
                value: string
              - name: description
                value: string
              - name: isEnabled
                value: boolean
              - name: ruleType
                value: string
              - name: minThreshold
                value: integer
              - name: maxThreshold
                value: integer
        - name: timeWindowRules
          value:
            - - name: minThreshold
                value: integer
              - name: maxThreshold
                value: integer
              - name: timeWindowSize
                value: string
        - name: allowlistRules
          value:
            - - name: valueType
                value: string
              - name: allowlistValues
                value:
                  - string
        - name: denylistRules
          value:
            - - name: valueType
                value: string
              - name: denylistValues
                value:
                  - string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>device_security_groups</code> resource.

```sql
/*+ delete */
DELETE FROM azure.security.device_security_groups
WHERE deviceSecurityGroupName = '{{ deviceSecurityGroupName }}'
AND resourceId = '{{ resourceId }}';
```
