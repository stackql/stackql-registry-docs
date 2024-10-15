---
title: apps
hide_title: false
hide_table_of_contents: false
keywords:
  - apps
  - spring_apps
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

Creates, updates, deletes, gets or lists a <code>apps</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>apps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.apps" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_apps', value: 'view', },
        { label: 'apps', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="addon_configs" /> | `text` | field from the `properties` object |
| <CopyableCode code="appName" /> | `text` | field from the `properties` object |
| <CopyableCode code="custom_persistent_disks" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_end_to_end_tls" /> | `text` | field from the `properties` object |
| <CopyableCode code="fqdn" /> | `text` | field from the `properties` object |
| <CopyableCode code="https_only" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Managed identity properties retrieved from ARM request headers. |
| <CopyableCode code="ingress_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="loaded_certificates" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The GEO location of the application, always the same with its parent resource |
| <CopyableCode code="persistent_disk" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="secrets" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="temporary_disk" /> | `text` | field from the `properties` object |
| <CopyableCode code="test_endpoint_auth_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="url" /> | `text` | field from the `properties` object |
| <CopyableCode code="vnet_addons" /> | `text` | field from the `properties` object |
| <CopyableCode code="workload_profile_name" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed identity properties retrieved from ARM request headers. |
| <CopyableCode code="location" /> | `string` | The GEO location of the application, always the same with its parent resource |
| <CopyableCode code="properties" /> | `object` | App resource properties payload |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="appName, resourceGroupName, serviceName, subscriptionId" /> | Get an App and its properties. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Handles requests to list all resources in a Service. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="appName, resourceGroupName, serviceName, subscriptionId" /> | Create a new App or update an exiting App. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="appName, resourceGroupName, serviceName, subscriptionId" /> | Operation to delete an App. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="appName, resourceGroupName, serviceName, subscriptionId" /> | Operation to update an exiting App. |
| <CopyableCode code="set_active_deployments" /> | `EXEC` | <CopyableCode code="appName, resourceGroupName, serviceName, subscriptionId" /> | Set existing Deployment under the app as active |
| <CopyableCode code="validate_domain" /> | `EXEC` | <CopyableCode code="appName, resourceGroupName, serviceName, subscriptionId, data__name" /> | Check the resource name is valid as well as not in use. |

## `SELECT` examples

Handles requests to list all resources in a Service.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_apps', value: 'view', },
        { label: 'apps', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
addon_configs,
appName,
custom_persistent_disks,
enable_end_to_end_tls,
fqdn,
https_only,
identity,
ingress_settings,
loaded_certificates,
location,
persistent_disk,
provisioning_state,
public,
resourceGroupName,
secrets,
serviceName,
subscriptionId,
temporary_disk,
test_endpoint_auth_state,
url,
vnet_addons,
workload_profile_name
FROM azure.spring_apps.vw_apps
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
location,
properties
FROM azure.spring_apps.apps
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>apps</code> resource.

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
INSERT INTO azure.spring_apps.apps (
appName,
resourceGroupName,
serviceName,
subscriptionId,
properties,
identity,
location
)
SELECT 
'{{ appName }}',
'{{ resourceGroupName }}',
'{{ serviceName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ identity }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: public
          value: boolean
        - name: url
          value: string
        - name: addonConfigs
          value: object
        - name: provisioningState
          value: string
        - name: fqdn
          value: string
        - name: httpsOnly
          value: boolean
        - name: temporaryDisk
          value:
            - name: sizeInGB
              value: integer
            - name: mountPath
              value: string
        - name: persistentDisk
          value:
            - name: sizeInGB
              value: integer
            - name: usedInGB
              value: integer
            - name: mountPath
              value: string
        - name: customPersistentDisks
          value: []
        - name: enableEndToEndTLS
          value: boolean
        - name: loadedCertificates
          value: []
        - name: vnetAddons
          value:
            - name: publicEndpoint
              value: boolean
            - name: publicEndpointUrl
              value: string
        - name: ingressSettings
          value:
            - name: readTimeoutInSeconds
              value: integer
            - name: sendTimeoutInSeconds
              value: integer
            - name: sessionAffinity
              value: string
            - name: sessionCookieMaxAge
              value: integer
            - name: backendProtocol
              value: string
            - name: clientAuth
              value:
                - name: certificates
                  value:
                    - string
        - name: secrets
          value:
            - - name: name
                value: string
              - name: value
                value: string
        - name: workloadProfileName
          value: string
        - name: testEndpointAuthState
          value: string
    - name: identity
      value:
        - name: type
          value: string
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: userAssignedIdentities
          value: []
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>apps</code> resource.

```sql
/*+ update */
UPDATE azure.spring_apps.apps
SET 
properties = '{{ properties }}',
identity = '{{ identity }}',
location = '{{ location }}'
WHERE 
appName = '{{ appName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>apps</code> resource.

```sql
/*+ delete */
DELETE FROM azure.spring_apps.apps
WHERE appName = '{{ appName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
