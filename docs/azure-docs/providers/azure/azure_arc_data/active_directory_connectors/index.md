---
title: active_directory_connectors
hide_title: false
hide_table_of_contents: false
keywords:
  - active_directory_connectors
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

Creates, updates, deletes, gets or lists a <code>active_directory_connectors</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>active_directory_connectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.azure_arc_data.active_directory_connectors" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_active_directory_connectors', value: 'view', },
        { label: 'active_directory_connectors', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="activeDirectoryConnectorName" /> | `text` | field from the `properties` object |
| <CopyableCode code="dataControllerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="domain_service_account_login_information" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="spec" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of an Active Directory connector resource |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="activeDirectoryConnectorName, dataControllerName, resourceGroupName, subscriptionId" /> | Retrieves an Active Directory connector resource |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="dataControllerName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="activeDirectoryConnectorName, dataControllerName, resourceGroupName, subscriptionId, data__properties" /> | Creates or replaces an Active Directory connector resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="activeDirectoryConnectorName, dataControllerName, resourceGroupName, subscriptionId" /> | Deletes an Active Directory connector resource |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_active_directory_connectors', value: 'view', },
        { label: 'active_directory_connectors', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
activeDirectoryConnectorName,
dataControllerName,
domain_service_account_login_information,
provisioning_state,
resourceGroupName,
spec,
status,
subscriptionId
FROM azure.azure_arc_data.vw_active_directory_connectors
WHERE dataControllerName = '{{ dataControllerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.azure_arc_data.active_directory_connectors
WHERE dataControllerName = '{{ dataControllerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>active_directory_connectors</code> resource.

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
INSERT INTO azure.azure_arc_data.active_directory_connectors (
activeDirectoryConnectorName,
dataControllerName,
resourceGroupName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ activeDirectoryConnectorName }}',
'{{ dataControllerName }}',
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
    - name: properties
      value:
        - name: domainServiceAccountLoginInformation
          value:
            - name: username
              value: string
            - name: password
              value: string
        - name: provisioningState
          value: string
        - name: spec
          value:
            - name: activeDirectory
              value:
                - name: realm
                  value: string
                - name: netbiosDomainName
                  value: string
                - name: serviceAccountProvisioning
                  value: string
                - name: ouDistinguishedName
                  value: string
                - name: domainControllers
                  value:
                    - name: primaryDomainController
                      value:
                        - name: hostname
                          value: string
                    - name: secondaryDomainControllers
                      value: []
            - name: dns
              value:
                - name: domainName
                  value: string
                - name: nameserverIPAddresses
                  value:
                    - string
                - name: replicas
                  value: integer
                - name: preferK8sDnsForPtrLookups
                  value: boolean
        - name: status
          value:
            - name: lastUpdateTime
              value: string
            - name: observedGeneration
              value: integer
            - name: state
              value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>active_directory_connectors</code> resource.

```sql
/*+ delete */
DELETE FROM azure.azure_arc_data.active_directory_connectors
WHERE activeDirectoryConnectorName = '{{ activeDirectoryConnectorName }}'
AND dataControllerName = '{{ dataControllerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
