---
title: portal_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - portal_configs
  - api_management
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

Creates, updates, deletes, gets or lists a <code>portal_configs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>portal_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.portal_configs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_portal_configs', value: 'view', },
        { label: 'portal_configs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="cors" /> | `text` | field from the `properties` object |
| <CopyableCode code="csp" /> | `text` | field from the `properties` object |
| <CopyableCode code="delegation" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_basic_auth" /> | `text` | field from the `properties` object |
| <CopyableCode code="portalConfigId" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="signin" /> | `text` | field from the `properties` object |
| <CopyableCode code="signup" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The developer portal configuration contract properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="portalConfigId, resourceGroupName, serviceName, subscriptionId" /> | Get the developer portal configuration. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Lists the developer portal configurations. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="If-Match, portalConfigId, resourceGroupName, serviceName, subscriptionId" /> | Create or update the developer portal configuration. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="If-Match, portalConfigId, resourceGroupName, serviceName, subscriptionId" /> | Update the developer portal configuration. |

## `SELECT` examples

Lists the developer portal configurations.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_portal_configs', value: 'view', },
        { label: 'portal_configs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
cors,
csp,
delegation,
enable_basic_auth,
portalConfigId,
resourceGroupName,
serviceName,
signin,
signup,
subscriptionId
FROM azure.api_management.vw_portal_configs
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.api_management.portal_configs
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>portal_configs</code> resource.

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
INSERT INTO azure.api_management.portal_configs (
If-Match,
portalConfigId,
resourceGroupName,
serviceName,
subscriptionId,
properties
)
SELECT 
'{{ If-Match }}',
'{{ portalConfigId }}',
'{{ resourceGroupName }}',
'{{ serviceName }}',
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
        - name: enableBasicAuth
          value: boolean
        - name: signin
          value:
            - name: require
              value: boolean
        - name: signup
          value:
            - name: termsOfService
              value:
                - name: text
                  value: string
                - name: requireConsent
                  value: boolean
        - name: delegation
          value:
            - name: delegateRegistration
              value: boolean
            - name: delegateSubscription
              value: boolean
            - name: delegationUrl
              value: string
            - name: validationKey
              value: string
        - name: cors
          value:
            - name: allowedOrigins
              value:
                - string
        - name: csp
          value:
            - name: mode
              value: string
            - name: reportUri
              value:
                - string
            - name: allowedSources
              value:
                - string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>portal_configs</code> resource.

```sql
/*+ update */
UPDATE azure.api_management.portal_configs
SET 
properties = '{{ properties }}'
WHERE 
If-Match = '{{ If-Match }}'
AND portalConfigId = '{{ portalConfigId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
