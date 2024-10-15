---
title: devices_security_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - devices_security_settings
  - storsimple_1200_series
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

Creates, updates, deletes, gets or lists a <code>devices_security_settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>devices_security_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_1200_series.devices_security_settings" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates the security settings. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>devices_security_settings</code> resource.

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
INSERT INTO azure_extras.storsimple_1200_series.devices_security_settings (
deviceName,
managerName,
resourceGroupName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ deviceName }}',
'{{ managerName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
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
    - name: type
      value: string
    - name: properties
      value:
        - name: deviceAdminPassword
          value:
            - name: value
              value: string
            - name: encryptionCertificateThumbprint
              value: string
            - name: encryptionAlgorithm
              value: string

```
</TabItem>
</Tabs>
