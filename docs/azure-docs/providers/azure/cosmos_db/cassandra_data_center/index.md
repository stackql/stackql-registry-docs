---
title: cassandra_data_center
hide_title: false
hide_table_of_contents: false
keywords:
  - cassandra_data_center
  - cosmos_db
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

Creates, updates, deletes, gets or lists a <code>cassandra_data_center</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cassandra_data_center</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmos_db.cassandra_data_center" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The unique resource identifier of the database account. |
| <CopyableCode code="name" /> | `string` | The name of the database account. |
| <CopyableCode code="properties" /> | `object` | Properties of a managed Cassandra data center. |
| <CopyableCode code="type" /> | `string` | The type of Azure resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, dataCenterName, resourceGroupName, subscriptionId" /> | Get the properties of a managed Cassandra data center. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | List all data centers in a particular managed Cassandra cluster. |
| <CopyableCode code="create_update" /> | `INSERT` | <CopyableCode code="clusterName, dataCenterName, resourceGroupName, subscriptionId" /> | Create or update a managed Cassandra data center. When updating, overwrite all properties. To update only some properties, use PATCH. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, dataCenterName, resourceGroupName, subscriptionId" /> | Delete a managed Cassandra data center. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="clusterName, dataCenterName, resourceGroupName, subscriptionId" /> | Update some of the properties of a managed Cassandra data center. |

## `SELECT` examples

List all data centers in a particular managed Cassandra cluster.


```sql
SELECT
id,
name,
properties,
type
FROM azure.cosmos_db.cassandra_data_center
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>cassandra_data_center</code> resource.

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
INSERT INTO azure.cosmos_db.cassandra_data_center (
clusterName,
dataCenterName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ clusterName }}',
'{{ dataCenterName }}',
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
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: properties
      value:
        - name: provisioningState
          value: []
        - name: dataCenterLocation
          value: string
        - name: delegatedSubnetId
          value: string
        - name: nodeCount
          value: integer
        - name: seedNodes
          value:
            - - name: ipAddress
                value: string
        - name: base64EncodedCassandraYamlFragment
          value: string
        - name: managedDiskCustomerKeyUri
          value: string
        - name: backupStorageCustomerKeyUri
          value: string
        - name: sku
          value: string
        - name: diskSku
          value: string
        - name: diskCapacity
          value: integer
        - name: availabilityZone
          value: boolean
        - name: authenticationMethodLdapProperties
          value:
            - name: serverHostname
              value: string
            - name: serverPort
              value: integer
            - name: serviceUserDistinguishedName
              value: string
            - name: serviceUserPassword
              value: string
            - name: searchBaseDistinguishedName
              value: string
            - name: searchFilterTemplate
              value: string
            - name: serverCertificates
              value:
                - - name: pem
                    value: string
            - name: connectionTimeoutInMs
              value: integer
        - name: deallocated
          value: boolean
        - name: provisionError
          value:
            - name: code
              value: string
            - name: message
              value: string
            - name: target
              value: string
            - name: additionalErrorInfo
              value: string
        - name: privateEndpointIpAddress
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>cassandra_data_center</code> resource.

```sql
/*+ update */
UPDATE azure.cosmos_db.cassandra_data_center
SET 
properties = '{{ properties }}'
WHERE 
clusterName = '{{ clusterName }}'
AND dataCenterName = '{{ dataCenterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>cassandra_data_center</code> resource.

```sql
/*+ delete */
DELETE FROM azure.cosmos_db.cassandra_data_center
WHERE clusterName = '{{ clusterName }}'
AND dataCenterName = '{{ dataCenterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
