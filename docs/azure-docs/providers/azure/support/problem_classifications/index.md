---
title: problem_classifications
hide_title: false
hide_table_of_contents: false
keywords:
  - problem_classifications
  - support
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

Creates, updates, deletes, gets or lists a <code>problem_classifications</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>problem_classifications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.support.problem_classifications" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_problem_classifications', value: 'view', },
        { label: 'problem_classifications', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Id of the resource. |
| <CopyableCode code="name" /> | `text` | Name of the resource. |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="metadata" /> | `text` | field from the `properties` object |
| <CopyableCode code="parent_problem_classification" /> | `text` | field from the `properties` object |
| <CopyableCode code="problemClassificationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="secondary_consent_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Type of the resource 'Microsoft.Support/problemClassification'. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Id of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="properties" /> | `object` | Details about a problem classification available for an Azure service. |
| <CopyableCode code="type" /> | `string` | Type of the resource 'Microsoft.Support/problemClassification'. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="problemClassificationName, serviceName" /> | Get problem classification details for a specific Azure service. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="serviceName" /> | Lists all the problem classifications (categories) available for a specific Azure service. Always use the service and problem classifications obtained programmatically. This practice ensures that you always have the most recent set of service and problem classification Ids. |
| <CopyableCode code="classify_problems" /> | `EXEC` | <CopyableCode code="problemServiceName, subscriptionId, data__issueSummary" /> | Classify the right problem classifications (categories) available for a specific Azure service.  |

## `SELECT` examples

Lists all the problem classifications (categories) available for a specific Azure service. Always use the service and problem classifications obtained programmatically. This practice ensures that you always have the most recent set of service and problem classification Ids.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_problem_classifications', value: 'view', },
        { label: 'problem_classifications', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
display_name,
metadata,
parent_problem_classification,
problemClassificationName,
secondary_consent_enabled,
serviceName,
type
FROM azure.support.vw_problem_classifications
WHERE serviceName = '{{ serviceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.support.problem_classifications
WHERE serviceName = '{{ serviceName }}';
```
</TabItem></Tabs>

