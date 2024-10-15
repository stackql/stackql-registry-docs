---
title: ios_mam_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - ios_mam_policies
  - intune
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

Creates, updates, deletes, gets or lists a <code>ios_mam_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ios_mam_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.intune.ios_mam_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="location" /> | `string` | Resource Location |
| <CopyableCode code="properties" /> | `object` | Intune MAM iOS Policy Properties. |
| <CopyableCode code="tags" /> | `object` | Resource Tags |
| <CopyableCode code="type" /> | `string` | Resource type |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hostName" /> | Returns Intune iOSPolicies. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="hostName, policyName" /> | Creates or updates iOSMAMPolicy. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="hostName, policyName" /> | Delete Ios Policy |

## `SELECT` examples

Returns Intune iOSPolicies.


```sql
SELECT
id,
name,
location,
properties,
tags,
type
FROM azure_extras.intune.ios_mam_policies
WHERE hostName = '{{ hostName }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>ios_mam_policies</code> resource.

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
INSERT INTO azure_extras.intune.ios_mam_policies (
hostName,
policyName,
properties,
tags,
location
)
SELECT 
'{{ hostName }}',
'{{ policyName }}',
'{{ properties }}',
'{{ tags }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: friendlyName
          value: string
        - name: description
          value: string
        - name: appSharingFromLevel
          value: string
        - name: appSharingToLevel
          value: string
        - name: authentication
          value: string
        - name: clipboardSharingLevel
          value: string
        - name: dataBackup
          value: string
        - name: fileSharingSaveAs
          value: string
        - name: pin
          value: string
        - name: pinNumRetry
          value: integer
        - name: deviceCompliance
          value: string
        - name: managedBrowser
          value: string
        - name: accessRecheckOfflineTimeout
          value: string
        - name: accessRecheckOnlineTimeout
          value: string
        - name: offlineWipeTimeout
          value: string
        - name: numOfApps
          value: integer
        - name: groupStatus
          value: string
        - name: lastModifiedTime
          value: string
        - name: fileEncryptionLevel
          value: string
        - name: touchId
          value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>ios_mam_policies</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.intune.ios_mam_policies
WHERE hostName = '{{ hostName }}'
AND policyName = '{{ policyName }}';
```
