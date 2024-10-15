---
title: views
hide_title: false
hide_table_of_contents: false
keywords:
  - views
  - cost_management
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

Creates, updates, deletes, gets or lists a <code>views</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>views</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cost_management.views" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_views', value: 'view', },
        { label: 'views', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="accumulated" /> | `text` | field from the `properties` object |
| <CopyableCode code="chart" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_on" /> | `text` | field from the `properties` object |
| <CopyableCode code="currency" /> | `text` | field from the `properties` object |
| <CopyableCode code="date_range" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="e_tag" /> | `text` | field from the `properties` object |
| <CopyableCode code="kpis" /> | `text` | field from the `properties` object |
| <CopyableCode code="metric" /> | `text` | field from the `properties` object |
| <CopyableCode code="modified_on" /> | `text` | field from the `properties` object |
| <CopyableCode code="pivots" /> | `text` | field from the `properties` object |
| <CopyableCode code="query" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
| <CopyableCode code="viewName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="eTag" /> | `string` | eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not. |
| <CopyableCode code="properties" /> | `object` | The properties of the view. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="viewName" /> | Gets the view by view name. |
| <CopyableCode code="get_by_scope" /> | `SELECT` | <CopyableCode code="scope, viewName" /> | Gets the view for the defined scope by view name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Lists all views by tenant and object. |
| <CopyableCode code="list_by_scope" /> | `SELECT` | <CopyableCode code="scope" /> | Lists all views at the given scope. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="viewName" /> | The operation to create or update a view. Update operation requires latest eTag to be set in the request. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="viewName" /> | The operation to delete a view. |
| <CopyableCode code="delete_by_scope" /> | `DELETE` | <CopyableCode code="scope, viewName" /> | The operation to delete a view. |

## `SELECT` examples

Lists all views by tenant and object.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_views', value: 'view', },
        { label: 'views', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
accumulated,
chart,
created_on,
currency,
date_range,
display_name,
e_tag,
kpis,
metric,
modified_on,
pivots,
query,
scope,
type,
viewName
FROM azure.cost_management.vw_views
;
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
eTag,
properties,
type
FROM azure.cost_management.views
;
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>views</code> resource.

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
INSERT INTO azure.cost_management.views (
viewName,
eTag,
properties
)
SELECT 
'{{ viewName }}',
'{{ eTag }}',
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
    - name: eTag
      value: string
    - name: properties
      value:
        - name: displayName
          value: string
        - name: scope
          value: string
        - name: createdOn
          value: string
        - name: modifiedOn
          value: string
        - name: dateRange
          value: string
        - name: currency
          value: string
        - name: query
          value:
            - name: type
              value: string
            - name: timeframe
              value: string
            - name: timePeriod
              value:
                - name: from
                  value: string
                - name: to
                  value: string
            - name: dataSet
              value:
                - name: granularity
                  value: string
                - name: configuration
                  value:
                    - name: columns
                      value:
                        - string
                - name: aggregation
                  value: object
                - name: grouping
                  value:
                    - - name: type
                        value: []
                      - name: name
                        value: string
                - name: sorting
                  value:
                    - - name: direction
                        value: string
                      - name: name
                        value: string
                - name: filter
                  value:
                    - name: and
                      value:
                        - - name: and
                            value:
                              - - name: and
                                  value:
                                    - - name: and
                                        value:
                                          - - name: and
                                              value:
                                                - - name: and
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                                        - name: dimensions
                                                          value: []
                                                  - name: or
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                            - name: or
                                              value:
                                                - - name: and
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                                  - name: or
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                      - name: or
                                        value:
                                          - - name: and
                                              value:
                                                - - name: and
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                                  - name: or
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                            - name: or
                                              value:
                                                - - name: and
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                                  - name: or
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                - name: or
                                  value:
                                    - - name: and
                                        value:
                                          - - name: and
                                              value:
                                                - - name: and
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                                  - name: or
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                            - name: or
                                              value:
                                                - - name: and
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                                  - name: or
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                      - name: or
                                        value:
                                          - - name: and
                                              value:
                                                - - name: and
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                                  - name: or
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                            - name: or
                                              value:
                                                - - name: and
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                                  - name: or
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                          - name: or
                            value:
                              - - name: and
                                  value:
                                    - - name: and
                                        value:
                                          - - name: and
                                              value:
                                                - - name: and
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                                  - name: or
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                            - name: or
                                              value:
                                                - - name: and
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                                  - name: or
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                      - name: or
                                        value:
                                          - - name: and
                                              value:
                                                - - name: and
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                                  - name: or
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                            - name: or
                                              value:
                                                - - name: and
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                                  - name: or
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                - name: or
                                  value:
                                    - - name: and
                                        value:
                                          - - name: and
                                              value:
                                                - - name: and
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                                  - name: or
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                            - name: or
                                              value:
                                                - - name: and
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                                  - name: or
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                      - name: or
                                        value:
                                          - - name: and
                                              value:
                                                - - name: and
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                                  - name: or
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                            - name: or
                                              value:
                                                - - name: and
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                                  - name: or
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                    - name: or
                      value:
                        - - name: and
                            value:
                              - - name: and
                                  value:
                                    - - name: and
                                        value:
                                          - - name: and
                                              value:
                                                - - name: and
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                                  - name: or
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                            - name: or
                                              value:
                                                - - name: and
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                                  - name: or
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                      - name: or
                                        value:
                                          - - name: and
                                              value:
                                                - - name: and
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                                  - name: or
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                            - name: or
                                              value:
                                                - - name: and
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                                  - name: or
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                - name: or
                                  value:
                                    - - name: and
                                        value:
                                          - - name: and
                                              value:
                                                - - name: and
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                                  - name: or
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                            - name: or
                                              value:
                                                - - name: and
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                                  - name: or
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                      - name: or
                                        value:
                                          - - name: and
                                              value:
                                                - - name: and
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                                  - name: or
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                            - name: or
                                              value:
                                                - - name: and
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                                  - name: or
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                          - name: or
                            value:
                              - - name: and
                                  value:
                                    - - name: and
                                        value:
                                          - - name: and
                                              value:
                                                - - name: and
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                                  - name: or
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                            - name: or
                                              value:
                                                - - name: and
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                                  - name: or
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                      - name: or
                                        value:
                                          - - name: and
                                              value:
                                                - - name: and
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                                  - name: or
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                            - name: or
                                              value:
                                                - - name: and
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                                  - name: or
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                - name: or
                                  value:
                                    - - name: and
                                        value:
                                          - - name: and
                                              value:
                                                - - name: and
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                                  - name: or
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                            - name: or
                                              value:
                                                - - name: and
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                                  - name: or
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                      - name: or
                                        value:
                                          - - name: and
                                              value:
                                                - - name: and
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                                  - name: or
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                            - name: or
                                              value:
                                                - - name: and
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
                                                  - name: or
                                                    value:
                                                      - - name: and
                                                          value:
                                                            - []
                                                        - name: or
                                                          value:
                                                            - []
            - name: includeMonetaryCommitment
              value: boolean
        - name: chart
          value: string
        - name: accumulated
          value: string
        - name: metric
          value: string
        - name: kpis
          value:
            - - name: type
                value: string
              - name: id
                value: string
              - name: enabled
                value: boolean
        - name: pivots
          value:
            - - name: type
                value: string
              - name: name
                value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>views</code> resource.

```sql
/*+ delete */
DELETE FROM azure.cost_management.views
WHERE viewName = '{{ viewName }}';
```
