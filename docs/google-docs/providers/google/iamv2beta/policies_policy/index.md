---
title: policies_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - policies_policy
  - iamv2beta
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

Creates, updates, deletes, gets or lists a <code>policies_policy</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>policies_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.iamv2beta.policies_policy" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create_policy" /> | `INSERT` | <CopyableCode code="policiesId, policiesId1" /> | Creates a policy. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>policies_policy</code> resource.

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
INSERT INTO google.iamv2beta.policies_policy (
policiesId,
policiesId1,
name,
uid,
displayName,
annotations,
etag,
rules
)
SELECT 
'{{ policiesId }}',
'{{ policiesId1 }}',
'{{ name }}',
'{{ uid }}',
'{{ displayName }}',
'{{ annotations }}',
'{{ etag }}',
'{{ rules }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: uid
      value: string
    - name: kind
      value: string
    - name: displayName
      value: string
    - name: annotations
      value: object
    - name: etag
      value: string
    - name: createTime
      value: string
    - name: updateTime
      value: string
    - name: deleteTime
      value: string
    - name: rules
      value:
        - - name: denyRule
            value:
              - name: deniedPrincipals
                value:
                  - string
              - name: exceptionPrincipals
                value:
                  - string
              - name: deniedPermissions
                value:
                  - string
              - name: exceptionPermissions
                value:
                  - string
              - name: denialCondition
                value:
                  - name: expression
                    value: string
                  - name: title
                    value: string
                  - name: description
                    value: string
                  - name: location
                    value: string
          - name: description
            value: string

```
</TabItem>
</Tabs>
