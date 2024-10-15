---
title: views_by_scopes
hide_title: false
hide_table_of_contents: false
keywords:
  - views_by_scopes
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

Creates, updates, deletes, gets or lists a <code>views_by_scopes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>views_by_scopes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cost_management.views_by_scopes" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="scope, viewName" /> | The operation to create or update a view. Update operation requires latest eTag to be set in the request. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>views_by_scopes</code> resource.

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
INSERT INTO azure.cost_management.views_by_scopes (
scope,
viewName,
eTag,
properties
)
SELECT 
'{{ scope }}',
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
