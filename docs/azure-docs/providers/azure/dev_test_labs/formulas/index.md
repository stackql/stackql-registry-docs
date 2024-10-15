---
title: formulas
hide_title: false
hide_table_of_contents: false
keywords:
  - formulas
  - dev_test_labs
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

Creates, updates, deletes, gets or lists a <code>formulas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>formulas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_test_labs.formulas" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_formulas', value: 'view', },
        { label: 'formulas', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The identifier of the resource. |
| <CopyableCode code="name" /> | `text` | The name of the resource. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="author" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="formula_content" /> | `text` | field from the `properties` object |
| <CopyableCode code="labName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The location of the resource. |
| <CopyableCode code="os_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | The tags of the resource. |
| <CopyableCode code="type" /> | `text` | The type of the resource. |
| <CopyableCode code="unique_identifier" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier of the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="location" /> | `string` | The location of the resource. |
| <CopyableCode code="properties" /> | `object` | Properties of a formula. |
| <CopyableCode code="tags" /> | `object` | The tags of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="labName, name, resourceGroupName, subscriptionId" /> | Get formula. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="labName, resourceGroupName, subscriptionId" /> | List formulas in a given lab. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="labName, name, resourceGroupName, subscriptionId, data__properties" /> | Create or replace an existing formula. This operation can take a while to complete. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="labName, name, resourceGroupName, subscriptionId" /> | Delete formula. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="labName, name, resourceGroupName, subscriptionId" /> | Allows modifying tags of formulas. All other properties will be ignored. |

## `SELECT` examples

List formulas in a given lab.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_formulas', value: 'view', },
        { label: 'formulas', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
author,
creation_date,
formula_content,
labName,
location,
os_type,
provisioning_state,
resourceGroupName,
subscriptionId,
tags,
type,
unique_identifier,
vm
FROM azure.dev_test_labs.vw_formulas
WHERE labName = '{{ labName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
tags,
type
FROM azure.dev_test_labs.formulas
WHERE labName = '{{ labName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>formulas</code> resource.

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
INSERT INTO azure.dev_test_labs.formulas (
labName,
name,
resourceGroupName,
subscriptionId,
data__properties,
location,
tags,
properties
)
SELECT 
'{{ labName }}',
'{{ name }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ location }}',
'{{ tags }}',
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
    - name: location
      value: string
    - name: tags
      value: object
    - name: properties
      value:
        - name: description
          value: string
        - name: author
          value: string
        - name: osType
          value: string
        - name: creationDate
          value: string
        - name: formulaContent
          value:
            - name: properties
              value:
                - name: bulkCreationParameters
                  value:
                    - name: instanceCount
                      value: integer
                - name: notes
                  value: string
                - name: ownerObjectId
                  value: string
                - name: ownerUserPrincipalName
                  value: string
                - name: createdDate
                  value: string
                - name: customImageId
                  value: string
                - name: size
                  value: string
                - name: userName
                  value: string
                - name: password
                  value: string
                - name: sshKey
                  value: string
                - name: isAuthenticationWithSshKey
                  value: boolean
                - name: labSubnetName
                  value: string
                - name: labVirtualNetworkId
                  value: string
                - name: disallowPublicIpAddress
                  value: boolean
                - name: artifacts
                  value:
                    - - name: artifactId
                        value: string
                      - name: artifactTitle
                        value: string
                      - name: parameters
                        value:
                          - - name: name
                              value: string
                            - name: value
                              value: string
                      - name: status
                        value: string
                      - name: deploymentStatusMessage
                        value: string
                      - name: vmExtensionStatusMessage
                        value: string
                      - name: installTime
                        value: string
                - name: galleryImageReference
                  value:
                    - name: offer
                      value: string
                    - name: publisher
                      value: string
                    - name: sku
                      value: string
                    - name: osType
                      value: string
                    - name: version
                      value: string
                - name: planId
                  value: string
                - name: networkInterface
                  value:
                    - name: virtualNetworkId
                      value: string
                    - name: subnetId
                      value: string
                    - name: publicIpAddressId
                      value: string
                    - name: publicIpAddress
                      value: string
                    - name: privateIpAddress
                      value: string
                    - name: dnsName
                      value: string
                    - name: rdpAuthority
                      value: string
                    - name: sshAuthority
                      value: string
                    - name: sharedPublicIpAddressConfiguration
                      value:
                        - name: inboundNatRules
                          value:
                            - - name: transportProtocol
                                value: string
                              - name: frontendPort
                                value: integer
                              - name: backendPort
                                value: integer
                - name: expirationDate
                  value: string
                - name: allowClaim
                  value: boolean
                - name: storageType
                  value: string
                - name: environmentId
                  value: string
                - name: dataDiskParameters
                  value:
                    - - name: attachNewDataDiskOptions
                        value:
                          - name: diskSizeGiB
                            value: integer
                          - name: diskName
                            value: string
                          - name: diskType
                            value: string
                      - name: existingLabDiskId
                        value: string
                      - name: hostCaching
                        value: string
                - name: scheduleParameters
                  value:
                    - - name: properties
                        value:
                          - name: status
                            value: string
                          - name: taskType
                            value: string
                          - name: weeklyRecurrence
                            value:
                              - name: weekdays
                                value:
                                  - string
                              - name: time
                                value: string
                          - name: dailyRecurrence
                            value:
                              - name: time
                                value: string
                          - name: hourlyRecurrence
                            value:
                              - name: minute
                                value: integer
                          - name: timeZoneId
                            value: string
                          - name: notificationSettings
                            value:
                              - name: status
                                value: string
                              - name: timeInMinutes
                                value: integer
                              - name: webhookUrl
                                value: string
                              - name: emailRecipient
                                value: string
                              - name: notificationLocale
                                value: string
                          - name: targetResourceId
                            value: string
                      - name: name
                        value: string
                      - name: location
                        value: string
                      - name: tags
                        value: object
            - name: name
              value: string
            - name: location
              value: string
            - name: tags
              value: object
        - name: vm
          value:
            - name: labVmId
              value: string
        - name: provisioningState
          value: string
        - name: uniqueIdentifier
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>formulas</code> resource.

```sql
/*+ update */
UPDATE azure.dev_test_labs.formulas
SET 
tags = '{{ tags }}'
WHERE 
labName = '{{ labName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>formulas</code> resource.

```sql
/*+ delete */
DELETE FROM azure.dev_test_labs.formulas
WHERE labName = '{{ labName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
