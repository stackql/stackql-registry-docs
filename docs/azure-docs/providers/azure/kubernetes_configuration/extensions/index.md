---
title: extensions
hide_title: false
hide_table_of_contents: false
keywords:
  - extensions
  - kubernetes_configuration
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

Creates, updates, deletes, gets or lists a <code>extensions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>extensions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.kubernetes_configuration.extensions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Identity for the resource. |
| <CopyableCode code="plan" /> | `object` | Plan for the resource. |
| <CopyableCode code="properties" /> | `object` | Properties of an Extension resource |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, clusterResourceName, clusterRp, extensionName, resourceGroupName, subscriptionId" /> | Gets Kubernetes Cluster Extension. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="clusterName, clusterResourceName, clusterRp, resourceGroupName, subscriptionId" /> | List all Extensions in the cluster. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="clusterName, clusterResourceName, clusterRp, extensionName, resourceGroupName, subscriptionId" /> | Create a new Kubernetes Cluster Extension. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, clusterResourceName, clusterRp, extensionName, resourceGroupName, subscriptionId" /> | Delete a Kubernetes Cluster Extension. This will cause the Agent to Uninstall the extension from the cluster. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="clusterName, clusterResourceName, clusterRp, extensionName, resourceGroupName, subscriptionId" /> | Patch an existing Kubernetes Cluster Extension. |

## `SELECT` examples

List all Extensions in the cluster.


```sql
SELECT
identity,
plan,
properties,
systemData
FROM azure.kubernetes_configuration.extensions
WHERE clusterName = '{{ clusterName }}'
AND clusterResourceName = '{{ clusterResourceName }}'
AND clusterRp = '{{ clusterRp }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>extensions</code> resource.

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
INSERT INTO azure.kubernetes_configuration.extensions (
clusterName,
clusterResourceName,
clusterRp,
extensionName,
resourceGroupName,
subscriptionId,
properties,
identity,
systemData,
plan
)
SELECT 
'{{ clusterName }}',
'{{ clusterResourceName }}',
'{{ clusterRp }}',
'{{ extensionName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ identity }}',
'{{ systemData }}',
'{{ plan }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: extensionType
          value: string
        - name: autoUpgradeMinorVersion
          value: boolean
        - name: releaseTrain
          value: string
        - name: version
          value: string
        - name: scope
          value:
            - name: cluster
              value:
                - name: releaseNamespace
                  value: string
            - name: namespace
              value:
                - name: targetNamespace
                  value: string
        - name: configurationSettings
          value: object
        - name: configurationProtectedSettings
          value: object
        - name: currentVersion
          value: string
        - name: provisioningState
          value: []
        - name: statuses
          value:
            - - name: code
                value: string
              - name: displayStatus
                value: string
              - name: level
                value: string
              - name: message
                value: string
              - name: time
                value: string
        - name: errorInfo
          value:
            - name: code
              value: string
            - name: message
              value: string
            - name: target
              value: string
            - name: details
              value:
                - - name: code
                    value: string
                  - name: message
                    value: string
                  - name: target
                    value: string
                  - name: details
                    value:
                      - - name: code
                          value: string
                        - name: message
                          value: string
                        - name: target
                          value: string
                        - name: details
                          value:
                            - - name: code
                                value: string
                              - name: message
                                value: string
                              - name: target
                                value: string
                              - name: details
                                value:
                                  - - name: code
                                      value: string
                                    - name: message
                                      value: string
                                    - name: target
                                      value: string
                                    - name: details
                                      value:
                                        - - name: code
                                            value: string
                                          - name: message
                                            value: string
                                          - name: target
                                            value: string
                                          - name: details
                                            value:
                                              - - name: code
                                                  value: string
                                                - name: message
                                                  value: string
                                                - name: target
                                                  value: string
                                                - name: details
                                                  value:
                                                    - - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                      - name: target
                                                        value: string
                                                      - name: details
                                                        value:
                                                          - - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                            - name: target
                                                              value: string
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: additionalInfo
                                                              value:
                                                                - []
                                                      - name: additionalInfo
                                                        value:
                                                          - - name: type
                                                              value: string
                                                            - name: info
                                                              value: object
                                                - name: additionalInfo
                                                  value:
                                                    - - name: type
                                                        value: string
                                                      - name: info
                                                        value: object
                                          - name: additionalInfo
                                            value:
                                              - - name: type
                                                  value: string
                                                - name: info
                                                  value: object
                                    - name: additionalInfo
                                      value:
                                        - - name: type
                                            value: string
                                          - name: info
                                            value: object
                              - name: additionalInfo
                                value:
                                  - - name: type
                                      value: string
                                    - name: info
                                      value: object
                        - name: additionalInfo
                          value:
                            - - name: type
                                value: string
                              - name: info
                                value: object
                  - name: additionalInfo
                    value:
                      - - name: type
                          value: string
                        - name: info
                          value: object
            - name: additionalInfo
              value:
                - - name: type
                    value: string
                  - name: info
                    value: object
        - name: customLocationSettings
          value: object
        - name: packageUri
          value: string
        - name: aksAssignedIdentity
          value:
            - name: principalId
              value: string
            - name: tenantId
              value: string
            - name: type
              value: string
        - name: isSystemExtension
          value: boolean
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: string
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string
    - name: plan
      value:
        - name: name
          value: string
        - name: publisher
          value: string
        - name: product
          value: string
        - name: promotionCode
          value: string
        - name: version
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>extensions</code> resource.

```sql
/*+ update */
UPDATE azure.kubernetes_configuration.extensions
SET 
properties = '{{ properties }}'
WHERE 
clusterName = '{{ clusterName }}'
AND clusterResourceName = '{{ clusterResourceName }}'
AND clusterRp = '{{ clusterRp }}'
AND extensionName = '{{ extensionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>extensions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.kubernetes_configuration.extensions
WHERE clusterName = '{{ clusterName }}'
AND clusterResourceName = '{{ clusterResourceName }}'
AND clusterRp = '{{ clusterRp }}'
AND extensionName = '{{ extensionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
