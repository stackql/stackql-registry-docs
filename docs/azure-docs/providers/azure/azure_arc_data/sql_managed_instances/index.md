---
title: sql_managed_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_managed_instances
  - azure_arc_data
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

Creates, updates, deletes, gets or lists a <code>sql_managed_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sql_managed_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.azure_arc_data.sql_managed_instances" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_managed_instances', value: 'view', },
        { label: 'sql_managed_instances', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="active_directory_information" /> | `text` | field from the `properties` object |
| <CopyableCode code="admin" /> | `text` | field from the `properties` object |
| <CopyableCode code="basic_login_information" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_controller_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="extension_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="k8s_raw" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_uploaded_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="license_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The resource model definition representing SKU for Azure Managed Instance - Azure Arc |
| <CopyableCode code="sqlManagedInstanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | The complex type of the extended location. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of sqlManagedInstance. |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU for Azure Managed Instance - Azure Arc |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, sqlManagedInstanceName, subscriptionId" /> | Retrieves a SQL Managed Instance resource |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> |  |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all sqlManagedInstances in a resource group. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, sqlManagedInstanceName, subscriptionId, data__properties" /> | Creates or replaces a SQL Managed Instance resource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, sqlManagedInstanceName, subscriptionId" /> | Deletes a SQL Managed Instance resource |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, sqlManagedInstanceName, subscriptionId" /> | Updates a SQL Managed Instance resource |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_managed_instances', value: 'view', },
        { label: 'sql_managed_instances', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
active_directory_information,
admin,
basic_login_information,
cluster_id,
data_controller_id,
end_time,
extended_location,
extension_id,
k8s_raw,
last_uploaded_date,
license_type,
location,
provisioning_state,
resourceGroupName,
sku,
sqlManagedInstanceName,
start_time,
subscriptionId,
tags
FROM azure.azure_arc_data.vw_sql_managed_instances
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
extendedLocation,
location,
properties,
sku,
tags
FROM azure.azure_arc_data.sql_managed_instances
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sql_managed_instances</code> resource.

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
INSERT INTO azure.azure_arc_data.sql_managed_instances (
resourceGroupName,
sqlManagedInstanceName,
subscriptionId,
data__properties,
tags,
location,
properties,
extendedLocation,
sku
)
SELECT 
'{{ resourceGroupName }}',
'{{ sqlManagedInstanceName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ tags }}',
'{{ location }}',
'{{ properties }}',
'{{ extendedLocation }}',
'{{ sku }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: tags
      value: object
    - name: location
      value: string
    - name: properties
      value:
        - name: dataControllerId
          value: string
        - name: admin
          value: string
        - name: startTime
          value: string
        - name: endTime
          value: string
        - name: k8sRaw
          value:
            - name: spec
              value:
                - name: scheduling
                  value:
                    - name: default
                      value:
                        - name: resources
                          value:
                            - name: requests
                              value: object
                            - name: limits
                              value: object
                - name: replicas
                  value: integer
                - name: security
                  value:
                    - name: adminLoginSecret
                      value: string
                    - name: serviceCertificateSecret
                      value: string
                    - name: activeDirectory
                      value:
                        - name: connector
                          value:
                            - name: name
                              value: string
                            - name: namespace
                              value: string
                        - name: accountName
                          value: string
                        - name: keytabSecret
                          value: string
                        - name: encryptionTypes
                          value:
                            - string
                    - name: transparentDataEncryption
                      value:
                        - name: mode
                          value: string
                        - name: protectorSecret
                          value: string
                - name: settings
                  value:
                    - name: network
                      value:
                        - name: forceencryption
                          value: integer
                        - name: tlsciphers
                          value: string
                        - name: tlsprotocols
                          value: string
        - name: basicLoginInformation
          value:
            - name: username
              value: string
            - name: password
              value: string
        - name: lastUploadedDate
          value: string
        - name: provisioningState
          value: string
        - name: activeDirectoryInformation
          value:
            - name: keytabInformation
              value:
                - name: keytab
                  value: string
        - name: licenseType
          value: string
        - name: clusterId
          value: string
        - name: extensionId
          value: string
    - name: extendedLocation
      value:
        - name: name
          value: string
        - name: type
          value: []
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: string
        - name: dev
          value: boolean
        - name: size
          value: string
        - name: family
          value: string
        - name: capacity
          value: integer

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>sql_managed_instances</code> resource.

```sql
/*+ update */
UPDATE azure.azure_arc_data.sql_managed_instances
SET 
tags = '{{ tags }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND sqlManagedInstanceName = '{{ sqlManagedInstanceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>sql_managed_instances</code> resource.

```sql
/*+ delete */
DELETE FROM azure.azure_arc_data.sql_managed_instances
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sqlManagedInstanceName = '{{ sqlManagedInstanceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
