---
title: managed_instance_dtcs
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_instance_dtcs
  - sql
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

Creates, updates, deletes, gets or lists a <code>managed_instance_dtcs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_instance_dtcs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.managed_instance_dtcs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_instance_dtcs', value: 'view', },
        { label: 'managed_instance_dtcs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="dtcName" /> | `text` | field from the `properties` object |
| <CopyableCode code="dtc_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="dtc_host_name_dns_suffix" /> | `text` | field from the `properties` object |
| <CopyableCode code="external_dns_suffix_search_list" /> | `text` | field from the `properties` object |
| <CopyableCode code="managedInstanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="security_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of managed instance DTC. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dtcName, managedInstanceName, resourceGroupName, subscriptionId" /> | Gets managed instance DTC settings. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="dtcName, managedInstanceName, resourceGroupName, subscriptionId" /> | Updates managed instance DTC settings. |

## `SELECT` examples

Gets managed instance DTC settings.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_instance_dtcs', value: 'view', },
        { label: 'managed_instance_dtcs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
dtcName,
dtc_enabled,
dtc_host_name_dns_suffix,
external_dns_suffix_search_list,
managedInstanceName,
provisioning_state,
resourceGroupName,
security_settings,
subscriptionId
FROM azure.sql.vw_managed_instance_dtcs
WHERE dtcName = '{{ dtcName }}'
AND managedInstanceName = '{{ managedInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.sql.managed_instance_dtcs
WHERE dtcName = '{{ dtcName }}'
AND managedInstanceName = '{{ managedInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>managed_instance_dtcs</code> resource.

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
INSERT INTO azure.sql.managed_instance_dtcs (
dtcName,
managedInstanceName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ dtcName }}',
'{{ managedInstanceName }}',
'{{ resourceGroupName }}',
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
        - name: dtcEnabled
          value: boolean
        - name: securitySettings
          value:
            - name: transactionManagerCommunicationSettings
              value:
                - name: allowInboundEnabled
                  value: boolean
                - name: allowOutboundEnabled
                  value: boolean
                - name: authentication
                  value: string
            - name: xaTransactionsEnabled
              value: boolean
            - name: snaLu6point2TransactionsEnabled
              value: boolean
            - name: xaTransactionsDefaultTimeout
              value: integer
            - name: xaTransactionsMaximumTimeout
              value: integer
        - name: externalDnsSuffixSearchList
          value:
            - string
        - name: dtcHostNameDnsSuffix
          value: string
        - name: provisioningState
          value: string

```
</TabItem>
</Tabs>
