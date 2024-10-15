---
title: labs_environments
hide_title: false
hide_table_of_contents: false
keywords:
  - labs_environments
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

Creates, updates, deletes, gets or lists a <code>labs_environments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>labs_environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_test_labs.labs_environments" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Create virtual machines in a lab. This operation can take a while to complete. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>labs_environments</code> resource.

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
INSERT INTO azure.dev_test_labs.labs_environments (
name,
resourceGroupName,
subscriptionId,
properties,
name,
location,
tags
)
SELECT 
'{{ name }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ name }}',
'{{ location }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
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

```
</TabItem>
</Tabs>
