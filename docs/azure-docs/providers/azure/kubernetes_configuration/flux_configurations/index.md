---
title: flux_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - flux_configurations
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

Creates, updates, deletes, gets or lists a <code>flux_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>flux_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.kubernetes_configuration.flux_configurations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties to create a Flux Configuration resource |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, clusterResourceName, clusterRp, fluxConfigurationName, resourceGroupName, subscriptionId" /> | Gets details of the Flux Configuration. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="clusterName, clusterResourceName, clusterRp, resourceGroupName, subscriptionId" /> | List all Flux Configurations. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="clusterName, clusterResourceName, clusterRp, fluxConfigurationName, resourceGroupName, subscriptionId" /> | Create a new Kubernetes Flux Configuration. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, clusterResourceName, clusterRp, fluxConfigurationName, resourceGroupName, subscriptionId" /> | This will delete the YAML file used to set up the Flux Configuration, thus stopping future sync from the source repo. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="clusterName, clusterResourceName, clusterRp, fluxConfigurationName, resourceGroupName, subscriptionId" /> | Update an existing Kubernetes Flux Configuration. |

## `SELECT` examples

List all Flux Configurations.


```sql
SELECT
properties,
systemData
FROM azure.kubernetes_configuration.flux_configurations
WHERE clusterName = '{{ clusterName }}'
AND clusterResourceName = '{{ clusterResourceName }}'
AND clusterRp = '{{ clusterRp }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>flux_configurations</code> resource.

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
INSERT INTO azure.kubernetes_configuration.flux_configurations (
clusterName,
clusterResourceName,
clusterRp,
fluxConfigurationName,
resourceGroupName,
subscriptionId,
properties,
systemData
)
SELECT 
'{{ clusterName }}',
'{{ clusterResourceName }}',
'{{ clusterRp }}',
'{{ fluxConfigurationName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ systemData }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: scope
          value: []
        - name: namespace
          value: string
        - name: sourceKind
          value: []
        - name: suspend
          value: boolean
        - name: gitRepository
          value:
            - name: url
              value: string
            - name: timeoutInSeconds
              value: integer
            - name: syncIntervalInSeconds
              value: integer
            - name: repositoryRef
              value:
                - name: branch
                  value: string
                - name: tag
                  value: string
                - name: semver
                  value: string
                - name: commit
                  value: string
            - name: sshKnownHosts
              value: string
            - name: httpsUser
              value: string
            - name: httpsCACert
              value: string
            - name: localAuthRef
              value: string
        - name: bucket
          value:
            - name: url
              value: string
            - name: bucketName
              value: string
            - name: insecure
              value: boolean
            - name: timeoutInSeconds
              value: integer
            - name: syncIntervalInSeconds
              value: integer
            - name: accessKey
              value: string
            - name: localAuthRef
              value: string
        - name: azureBlob
          value:
            - name: url
              value: string
            - name: containerName
              value: string
            - name: timeoutInSeconds
              value: integer
            - name: syncIntervalInSeconds
              value: integer
            - name: servicePrincipal
              value:
                - name: clientId
                  value: string
                - name: tenantId
                  value: string
                - name: clientSecret
                  value: string
                - name: clientCertificate
                  value: string
                - name: clientCertificatePassword
                  value: string
                - name: clientCertificateSendChain
                  value: boolean
            - name: accountKey
              value: string
            - name: sasToken
              value: string
            - name: managedIdentity
              value:
                - name: clientId
                  value: string
            - name: localAuthRef
              value: string
        - name: ociRepository
          value:
            - name: url
              value: string
            - name: timeoutInSeconds
              value: integer
            - name: syncIntervalInSeconds
              value: integer
            - name: repositoryRef
              value:
                - name: tag
                  value: string
                - name: semver
                  value: string
                - name: digest
                  value: string
            - name: layerSelector
              value:
                - name: mediaType
                  value: string
                - name: operation
                  value: []
            - name: verify
              value:
                - name: provider
                  value: string
                - name: verificationConfig
                  value: object
                - name: matchOidcIdentity
                  value:
                    - - name: issuer
                        value: string
                      - name: subject
                        value: string
            - name: insecure
              value: boolean
            - name: useWorkloadIdentity
              value: boolean
            - name: serviceAccountName
              value: string
            - name: tlsConfig
              value:
                - name: clientCertificate
                  value: string
                - name: privateKey
                  value: string
                - name: caCertificate
                  value: string
            - name: localAuthRef
              value: string
        - name: kustomizations
          value: object
        - name: configurationProtectedSettings
          value: object
        - name: statuses
          value:
            - - name: name
                value: string
              - name: namespace
                value: string
              - name: kind
                value: string
              - name: complianceState
                value: []
              - name: appliedBy
                value:
                  - name: name
                    value: string
                  - name: namespace
                    value: string
              - name: statusConditions
                value:
                  - - name: lastTransitionTime
                      value: string
                    - name: message
                      value: string
                    - name: reason
                      value: string
                    - name: status
                      value: string
                    - name: type
                      value: string
              - name: helmReleaseProperties
                value:
                  - name: lastRevisionApplied
                    value: integer
                  - name: failureCount
                    value: integer
                  - name: installFailureCount
                    value: integer
                  - name: upgradeFailureCount
                    value: integer
        - name: repositoryPublicKey
          value: string
        - name: sourceSyncedCommitId
          value: string
        - name: sourceUpdatedAt
          value: string
        - name: statusUpdatedAt
          value: string
        - name: waitForReconciliation
          value: boolean
        - name: reconciliationWaitDuration
          value: string
        - name: provisioningState
          value: []
        - name: errorMessage
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

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>flux_configurations</code> resource.

```sql
/*+ update */
UPDATE azure.kubernetes_configuration.flux_configurations
SET 
properties = '{{ properties }}'
WHERE 
clusterName = '{{ clusterName }}'
AND clusterResourceName = '{{ clusterResourceName }}'
AND clusterRp = '{{ clusterRp }}'
AND fluxConfigurationName = '{{ fluxConfigurationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>flux_configurations</code> resource.

```sql
/*+ delete */
DELETE FROM azure.kubernetes_configuration.flux_configurations
WHERE clusterName = '{{ clusterName }}'
AND clusterResourceName = '{{ clusterResourceName }}'
AND clusterRp = '{{ clusterRp }}'
AND fluxConfigurationName = '{{ fluxConfigurationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
