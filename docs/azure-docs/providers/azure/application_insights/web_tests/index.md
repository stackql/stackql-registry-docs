---
title: web_tests
hide_title: false
hide_table_of_contents: false
keywords:
  - web_tests
  - application_insights
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

Creates, updates, deletes, gets or lists a <code>web_tests</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>web_tests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.application_insights.web_tests" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_web_tests', value: 'view', },
        { label: 'web_tests', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Azure resource Id |
| <CopyableCode code="name" /> | `text` | Azure resource name |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="frequency" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | The kind of WebTest that this web test watches. Choices are ping, multistep and standard. |
| <CopyableCode code="location" /> | `text` | Resource location |
| <CopyableCode code="locations" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="request" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="retry_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="synthetic_monitor_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags |
| <CopyableCode code="timeout" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Azure resource type |
| <CopyableCode code="validation_rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="webTestName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Azure resource Id |
| <CopyableCode code="name" /> | `string` | Azure resource name |
| <CopyableCode code="kind" /> | `string` | The kind of WebTest that this web test watches. Choices are ping, multistep and standard. |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | Metadata describing a web test for an Azure resource. |
| <CopyableCode code="tags" /> | `` | Resource tags |
| <CopyableCode code="type" /> | `string` | Azure resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, webTestName" /> | Get a specific Application Insights web test definition. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get all Application Insights web test definitions for the specified subscription. |
| <CopyableCode code="list_by_component" /> | `SELECT` | <CopyableCode code="componentName, resourceGroupName, subscriptionId" /> | Get all Application Insights web tests defined for the specified component. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get all Application Insights web tests defined for the specified resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, webTestName" /> | Creates or updates an Application Insights web test definition. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, webTestName" /> | Deletes an Application Insights web test. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, webTestName" /> | Updates the tags associated with an Application Insights web test. |

## `SELECT` examples

Get all Application Insights web test definitions for the specified subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_web_tests', value: 'view', },
        { label: 'web_tests', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
configuration,
enabled,
frequency,
kind,
location,
locations,
provisioning_state,
request,
resourceGroupName,
retry_enabled,
subscriptionId,
synthetic_monitor_id,
tags,
timeout,
type,
validation_rules,
webTestName
FROM azure.application_insights.vw_web_tests
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
kind,
location,
properties,
tags,
type
FROM azure.application_insights.web_tests
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>web_tests</code> resource.

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
INSERT INTO azure.application_insights.web_tests (
resourceGroupName,
subscriptionId,
webTestName,
location,
tags,
kind,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ webTestName }}',
'{{ location }}',
'{{ tags }}',
'{{ kind }}',
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
      value: string
    - name: kind
      value: string
    - name: properties
      value:
        - name: SyntheticMonitorId
          value: string
        - name: Name
          value: string
        - name: Description
          value: string
        - name: Enabled
          value: boolean
        - name: Frequency
          value: integer
        - name: Timeout
          value: integer
        - name: Kind
          value: string
        - name: RetryEnabled
          value: boolean
        - name: Locations
          value:
            - - name: Id
                value: string
        - name: Configuration
          value:
            - name: WebTest
              value: string
        - name: provisioningState
          value: string
        - name: Request
          value:
            - name: RequestUrl
              value: string
            - name: Headers
              value:
                - - name: key
                    value: string
                  - name: value
                    value: string
            - name: HttpVerb
              value: string
            - name: RequestBody
              value: string
            - name: ParseDependentRequests
              value: boolean
            - name: FollowRedirects
              value: boolean
        - name: ValidationRules
          value:
            - name: ContentValidation
              value:
                - name: ContentMatch
                  value: string
                - name: IgnoreCase
                  value: boolean
                - name: PassIfTextFound
                  value: boolean
            - name: SSLCheck
              value: boolean
            - name: SSLCertRemainingLifetimeCheck
              value: integer
            - name: ExpectedHttpStatusCode
              value: integer
            - name: IgnoreHttpStatusCode
              value: boolean

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>web_tests</code> resource.

```sql
/*+ delete */
DELETE FROM azure.application_insights.web_tests
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND webTestName = '{{ webTestName }}';
```
