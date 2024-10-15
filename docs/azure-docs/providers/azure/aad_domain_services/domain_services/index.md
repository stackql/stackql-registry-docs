---
title: domain_services
hide_title: false
hide_table_of_contents: false
keywords:
  - domain_services
  - aad_domain_services
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

Creates, updates, deletes, gets or lists a <code>domain_services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domain_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.aad_domain_services.domain_services" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_domain_services', value: 'view', },
        { label: 'domain_services', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="config_diagnostics" /> | `text` | field from the `properties` object |
| <CopyableCode code="deployment_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="domainServiceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="domain_configuration_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="domain_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="domain_security_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="filtered_sync" /> | `text` | field from the `properties` object |
| <CopyableCode code="ldaps_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="migration_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="notification_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="replica_sets" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_forest_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="sync_application_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="sync_owner" /> | `text` | field from the `properties` object |
| <CopyableCode code="sync_scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Properties of the Domain Service. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="domainServiceName, resourceGroupName, subscriptionId" /> | The Get Domain Service operation retrieves a json representation of the Domain Service. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | The List Domain Services in Subscription operation lists all the domain services available under the given subscription (and across all resource groups within that subscription). |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | The List Domain Services in Resource Group operation lists all the domain services available under the given resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="domainServiceName, resourceGroupName, subscriptionId" /> | The Create Domain Service operation creates a new domain service with the specified parameters. If the specific service already exists, then any patchable properties will be updated and any immutable properties will remain unchanged. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="domainServiceName, resourceGroupName, subscriptionId" /> | The Delete Domain Service operation deletes an existing Domain Service. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="domainServiceName, resourceGroupName, subscriptionId" /> | The Update Domain Service operation can be used to update the existing deployment. The update call only supports the properties listed in the PATCH body. |

## `SELECT` examples

The List Domain Services in Subscription operation lists all the domain services available under the given subscription (and across all resource groups within that subscription).

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_domain_services', value: 'view', },
        { label: 'domain_services', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
config_diagnostics,
deployment_id,
domainServiceName,
domain_configuration_type,
domain_name,
domain_security_settings,
filtered_sync,
ldaps_settings,
migration_properties,
notification_settings,
provisioning_state,
replica_sets,
resourceGroupName,
resource_forest_settings,
sku,
subscriptionId,
sync_application_id,
sync_owner,
sync_scope,
tenant_id,
type,
version
FROM azure.aad_domain_services.vw_domain_services
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.aad_domain_services.domain_services
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>domain_services</code> resource.

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
INSERT INTO azure.aad_domain_services.domain_services (
domainServiceName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ domainServiceName }}',
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
        - name: version
          value: integer
        - name: tenantId
          value: string
        - name: domainName
          value: string
        - name: deploymentId
          value: string
        - name: syncOwner
          value: string
        - name: syncApplicationId
          value: string
        - name: replicaSets
          value:
            - - name: replicaSetId
                value: string
              - name: location
                value: string
              - name: vnetSiteId
                value: string
              - name: subnetId
                value: string
              - name: domainControllerIpAddress
                value:
                  - string
              - name: externalAccessIpAddress
                value: string
              - name: serviceStatus
                value: string
              - name: healthLastEvaluated
                value: string
              - name: healthMonitors
                value:
                  - - name: id
                      value: string
                    - name: name
                      value: string
                    - name: details
                      value: string
              - name: healthAlerts
                value:
                  - - name: id
                      value: string
                    - name: name
                      value: string
                    - name: issue
                      value: string
                    - name: severity
                      value: string
                    - name: raised
                      value: string
                    - name: lastDetected
                      value: string
                    - name: resolutionUri
                      value: string
        - name: ldapsSettings
          value:
            - name: ldaps
              value: string
            - name: pfxCertificate
              value: string
            - name: pfxCertificatePassword
              value: string
            - name: publicCertificate
              value: string
            - name: certificateThumbprint
              value: string
            - name: certificateNotAfter
              value: string
            - name: externalAccess
              value: string
        - name: resourceForestSettings
          value:
            - name: settings
              value:
                - - name: trustedDomainFqdn
                    value: string
                  - name: trustDirection
                    value: string
                  - name: friendlyName
                    value: string
                  - name: remoteDnsIps
                    value: string
                  - name: trustPassword
                    value: string
            - name: resourceForest
              value: string
        - name: domainSecuritySettings
          value:
            - name: ntlmV1
              value: string
            - name: tlsV1
              value: string
            - name: syncNtlmPasswords
              value: string
            - name: syncKerberosPasswords
              value: string
            - name: syncOnPremPasswords
              value: string
            - name: kerberosRc4Encryption
              value: string
            - name: kerberosArmoring
              value: string
            - name: ldapSigning
              value: string
            - name: channelBinding
              value: string
        - name: domainConfigurationType
          value: string
        - name: sku
          value: string
        - name: filteredSync
          value: string
        - name: syncScope
          value: string
        - name: notificationSettings
          value:
            - name: notifyGlobalAdmins
              value: string
            - name: notifyDcAdmins
              value: string
            - name: additionalRecipients
              value:
                - string
        - name: migrationProperties
          value:
            - name: oldSubnetId
              value: string
            - name: oldVnetSiteId
              value: string
            - name: migrationProgress
              value:
                - name: completionPercentage
                  value: number
                - name: progressMessage
                  value: string
        - name: provisioningState
          value: string
        - name: configDiagnostics
          value:
            - name: lastExecuted
              value: string
            - name: validatorResults
              value:
                - - name: validatorId
                    value: string
                  - name: replicaSetSubnetDisplayName
                    value: string
                  - name: status
                    value: string
                  - name: issues
                    value:
                      - - name: id
                          value: string
                        - name: descriptionParams
                          value:
                            - string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>domain_services</code> resource.

```sql
/*+ update */
UPDATE azure.aad_domain_services.domain_services
SET 
properties = '{{ properties }}'
WHERE 
domainServiceName = '{{ domainServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>domain_services</code> resource.

```sql
/*+ delete */
DELETE FROM azure.aad_domain_services.domain_services
WHERE domainServiceName = '{{ domainServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
