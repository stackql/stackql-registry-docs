---
title: apps
hide_title: false
hide_table_of_contents: false
keywords:
  - apps
  - apps
  - digitalocean
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage digitalocean resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>apps</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>apps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.apps.apps" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="active_deployment" /> | `object` |  |
| <CopyableCode code="created_at" /> | `string` |  |
| <CopyableCode code="dedicated_ips" /> | `array` |  |
| <CopyableCode code="default_ingress" /> | `string` |  |
| <CopyableCode code="domains" /> | `array` |  |
| <CopyableCode code="in_progress_deployment" /> | `object` |  |
| <CopyableCode code="last_deployment_created_at" /> | `string` |  |
| <CopyableCode code="live_domain" /> | `string` |  |
| <CopyableCode code="live_url" /> | `string` |  |
| <CopyableCode code="live_url_base" /> | `string` |  |
| <CopyableCode code="owner_uuid" /> | `string` |  |
| <CopyableCode code="pending_deployment" /> | `object` | The most recent pending deployment. For CreateApp and UpdateApp transactions this is guaranteed to reflect the associated deployment. |
| <CopyableCode code="pinned_deployment" /> | `object` | The deployment that the app is pinned to. |
| <CopyableCode code="project_id" /> | `string` |  |
| <CopyableCode code="region" /> | `object` |  |
| <CopyableCode code="spec" /> | `object` | The desired configuration of an application. |
| <CopyableCode code="tier_slug" /> | `string` |  |
| <CopyableCode code="updated_at" /> | `string` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="apps_get" /> | `SELECT` | <CopyableCode code="id" /> | Retrieve details about an existing app by either its ID or name. To retrieve an app by its name, do not include an ID in the request path. Information about the current active deployment as well as any in progress ones will also be included in the response. |
| <CopyableCode code="apps_list" /> | `SELECT` | <CopyableCode code="" /> | List all apps on your account. Information about the current active deployment as well as any in progress ones will also be included for each app. |
| <CopyableCode code="apps_create" /> | `INSERT` | <CopyableCode code="data__spec" /> | Create a new app by submitting an app specification. For documentation on app specifications (`AppSpec` objects), please refer to [the product documentation](https://docs.digitalocean.com/products/app-platform/reference/app-spec/). |
| <CopyableCode code="apps_delete" /> | `DELETE` | <CopyableCode code="id" /> | Delete an existing app. Once deleted, all active deployments will be permanently shut down and the app deleted. If needed, be sure to back up your app specification so that you may re-create it at a later time. |
| <CopyableCode code="apps_update" /> | `EXEC` | <CopyableCode code="id, data__spec" /> | Update an existing app by submitting a new app specification. For documentation on app specifications (`AppSpec` objects), please refer to [the product documentation](https://docs.digitalocean.com/products/app-platform/reference/app-spec/). |
| <CopyableCode code="apps_validate_app_spec" /> | `EXEC` | <CopyableCode code="data__spec" /> | To propose and validate a spec for a new or existing app, send a POST request to the `/v2/apps/propose` endpoint. The request returns some information about the proposed app, including app cost and upgrade cost. If an existing app ID is specified, the app spec is treated as a proposed update to the existing app. |

## `SELECT` examples

List all apps on your account. Information about the current active deployment as well as any in progress ones will also be included for each app.


```sql
SELECT
id,
active_deployment,
created_at,
dedicated_ips,
default_ingress,
domains,
in_progress_deployment,
last_deployment_created_at,
live_domain,
live_url,
live_url_base,
owner_uuid,
pending_deployment,
pinned_deployment,
project_id,
region,
spec,
tier_slug,
updated_at
FROM digitalocean.apps.apps
;
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>apps</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'Required Properties', value: 'required' },
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO digitalocean.apps.apps (
data__spec,
data__project_id
)
SELECT 
'{{ spec }}',
'{{ project_id }}'
;
```
</TabItem>

<TabItem value="required">

```sql
/*+ create */
INSERT INTO digitalocean.apps.apps (
data__spec
)
SELECT 
'{{ spec }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: apps
  props:
    - name: data__spec
      value: string
    - name: spec
      props:
        - name: name
          value: string
        - name: region
          value: string
        - name: domains
          value: array
          props:
            - name: domain
              value: string
            - name: type
              value: string
            - name: wildcard
              value: boolean
            - name: zone
              value: string
            - name: minimum_tls_version
              value: string
        - name: services
          value: array
          props:
            - name: name
              value: string
            - name: git
              props:
                - name: branch
                  value: string
                - name: repo_clone_url
                  value: string
            - name: github
              props:
                - name: branch
                  value: string
                - name: deploy_on_push
                  value: boolean
                - name: repo
                  value: string
            - name: gitlab
              props:
                - name: branch
                  value: string
                - name: deploy_on_push
                  value: boolean
                - name: repo
                  value: string
            - name: image
              props:
                - name: registry
                  value: string
                - name: registry_type
                  value: string
                - name: registry_credentials
                  value: string
                - name: repository
                  value: string
                - name: tag
                  value: string
                - name: digest
                  value: string
                - name: deploy_on_push
                  props:
                    - name: enabled
                      value: boolean
            - name: dockerfile_path
              value: string
            - name: build_command
              value: string
            - name: run_command
              value: string
            - name: source_dir
              value: string
            - name: envs
              value: array
              props:
                - name: key
                  value: string
                - name: scope
                  value: string
                - name: type
                  value: string
                - name: value
                  value: string
            - name: environment_slug
              value: string
            - name: log_destinations
              value: array
              props:
                - name: name
                  value: string
                - name: papertrail
                  props:
                    - name: endpoint
                      value: string
                - name: datadog
                  props:
                    - name: endpoint
                      value: string
                    - name: api_key
                      value: string
                - name: logtail
                  props:
                    - name: token
                      value: string
                - name: open_search
                  props:
                    - name: endpoint
                      value: string
                    - name: basic_auth
                      props:
                        - name: user
                          value: string
                        - name: password
                          value: string
                    - name: index_name
                      value: string
                    - name: cluster_name
                      value: string
            - name: instance_count
              value: integer
            - name: instance_size_slug
              value: string
            - name: autoscaling
              props:
                - name: min_instance_count
                  value: integer
                - name: max_instance_count
                  value: integer
                - name: metrics
                  props:
                    - name: cpu
                      props:
                        - name: percent
                          value: integer
            - name: cors
              props:
                - name: allow_origins
                  value: array
                  props:
                    - name: exact
                      value: string
                    - name: prefix
                      value: string
                    - name: regex
                      value: string
                - name: allow_methods
                  value: array
                - name: allow_headers
                  value: array
                - name: expose_headers
                  value: array
                - name: max_age
                  value: string
                - name: allow_credentials
                  value: boolean
            - name: health_check
              props:
                - name: failure_threshold
                  value: integer
                - name: port
                  value: integer
                - name: http_path
                  value: string
                - name: initial_delay_seconds
                  value: integer
                - name: period_seconds
                  value: integer
                - name: success_threshold
                  value: integer
                - name: timeout_seconds
                  value: integer
            - name: protocol
              value: string
            - name: http_port
              value: integer
            - name: internal_ports
              value: array
            - name: routes
              value: array
              props:
                - name: path
                  value: string
                - name: preserve_path_prefix
                  value: boolean
            - name: termination
              props:
                - name: drain_seconds
                  value: integer
                - name: grace_period_seconds
                  value: integer
        - name: static_sites
          value: array
          props:
            - name: name
              value: string
            - name: git
              props:
                - name: branch
                  value: string
                - name: repo_clone_url
                  value: string
            - name: github
              props:
                - name: branch
                  value: string
                - name: deploy_on_push
                  value: boolean
                - name: repo
                  value: string
            - name: gitlab
              props:
                - name: branch
                  value: string
                - name: deploy_on_push
                  value: boolean
                - name: repo
                  value: string
            - name: image
              props:
                - name: registry
                  value: string
                - name: registry_type
                  value: string
                - name: registry_credentials
                  value: string
                - name: repository
                  value: string
                - name: tag
                  value: string
                - name: digest
                  value: string
                - name: deploy_on_push
                  props:
                    - name: enabled
                      value: boolean
            - name: dockerfile_path
              value: string
            - name: build_command
              value: string
            - name: run_command
              value: string
            - name: source_dir
              value: string
            - name: envs
              value: array
              props:
                - name: key
                  value: string
                - name: scope
                  value: string
                - name: type
                  value: string
                - name: value
                  value: string
            - name: environment_slug
              value: string
            - name: log_destinations
              value: array
              props:
                - name: name
                  value: string
                - name: papertrail
                  props:
                    - name: endpoint
                      value: string
                - name: datadog
                  props:
                    - name: endpoint
                      value: string
                    - name: api_key
                      value: string
                - name: logtail
                  props:
                    - name: token
                      value: string
                - name: open_search
                  props:
                    - name: endpoint
                      value: string
                    - name: basic_auth
                      props:
                        - name: user
                          value: string
                        - name: password
                          value: string
                    - name: index_name
                      value: string
                    - name: cluster_name
                      value: string
            - name: index_document
              value: string
            - name: error_document
              value: string
            - name: catchall_document
              value: string
            - name: output_dir
              value: string
            - name: cors
              props:
                - name: allow_origins
                  value: array
                  props:
                    - name: exact
                      value: string
                    - name: prefix
                      value: string
                    - name: regex
                      value: string
                - name: allow_methods
                  value: array
                - name: allow_headers
                  value: array
                - name: expose_headers
                  value: array
                - name: max_age
                  value: string
                - name: allow_credentials
                  value: boolean
            - name: routes
              value: array
              props:
                - name: path
                  value: string
                - name: preserve_path_prefix
                  value: boolean
        - name: jobs
          value: array
          props:
            - name: name
              value: string
            - name: git
              props:
                - name: branch
                  value: string
                - name: repo_clone_url
                  value: string
            - name: github
              props:
                - name: branch
                  value: string
                - name: deploy_on_push
                  value: boolean
                - name: repo
                  value: string
            - name: gitlab
              props:
                - name: branch
                  value: string
                - name: deploy_on_push
                  value: boolean
                - name: repo
                  value: string
            - name: image
              props:
                - name: registry
                  value: string
                - name: registry_type
                  value: string
                - name: registry_credentials
                  value: string
                - name: repository
                  value: string
                - name: tag
                  value: string
                - name: digest
                  value: string
                - name: deploy_on_push
                  props:
                    - name: enabled
                      value: boolean
            - name: dockerfile_path
              value: string
            - name: build_command
              value: string
            - name: run_command
              value: string
            - name: source_dir
              value: string
            - name: envs
              value: array
              props:
                - name: key
                  value: string
                - name: scope
                  value: string
                - name: type
                  value: string
                - name: value
                  value: string
            - name: environment_slug
              value: string
            - name: log_destinations
              value: array
              props:
                - name: name
                  value: string
                - name: papertrail
                  props:
                    - name: endpoint
                      value: string
                - name: datadog
                  props:
                    - name: endpoint
                      value: string
                    - name: api_key
                      value: string
                - name: logtail
                  props:
                    - name: token
                      value: string
                - name: open_search
                  props:
                    - name: endpoint
                      value: string
                    - name: basic_auth
                      props:
                        - name: user
                          value: string
                        - name: password
                          value: string
                    - name: index_name
                      value: string
                    - name: cluster_name
                      value: string
            - name: instance_count
              value: integer
            - name: instance_size_slug
              value: string
            - name: autoscaling
              props:
                - name: min_instance_count
                  value: integer
                - name: max_instance_count
                  value: integer
                - name: metrics
                  props:
                    - name: cpu
                      props:
                        - name: percent
                          value: integer
            - name: kind
              value: string
            - name: termination
              props:
                - name: grace_period_seconds
                  value: integer
        - name: workers
          value: array
          props:
            - name: name
              value: string
            - name: git
              props:
                - name: branch
                  value: string
                - name: repo_clone_url
                  value: string
            - name: github
              props:
                - name: branch
                  value: string
                - name: deploy_on_push
                  value: boolean
                - name: repo
                  value: string
            - name: gitlab
              props:
                - name: branch
                  value: string
                - name: deploy_on_push
                  value: boolean
                - name: repo
                  value: string
            - name: image
              props:
                - name: registry
                  value: string
                - name: registry_type
                  value: string
                - name: registry_credentials
                  value: string
                - name: repository
                  value: string
                - name: tag
                  value: string
                - name: digest
                  value: string
                - name: deploy_on_push
                  props:
                    - name: enabled
                      value: boolean
            - name: dockerfile_path
              value: string
            - name: build_command
              value: string
            - name: run_command
              value: string
            - name: source_dir
              value: string
            - name: envs
              value: array
              props:
                - name: key
                  value: string
                - name: scope
                  value: string
                - name: type
                  value: string
                - name: value
                  value: string
            - name: environment_slug
              value: string
            - name: log_destinations
              value: array
              props:
                - name: name
                  value: string
                - name: papertrail
                  props:
                    - name: endpoint
                      value: string
                - name: datadog
                  props:
                    - name: endpoint
                      value: string
                    - name: api_key
                      value: string
                - name: logtail
                  props:
                    - name: token
                      value: string
                - name: open_search
                  props:
                    - name: endpoint
                      value: string
                    - name: basic_auth
                      props:
                        - name: user
                          value: string
                        - name: password
                          value: string
                    - name: index_name
                      value: string
                    - name: cluster_name
                      value: string
            - name: instance_count
              value: integer
            - name: instance_size_slug
              value: string
            - name: autoscaling
              props:
                - name: min_instance_count
                  value: integer
                - name: max_instance_count
                  value: integer
                - name: metrics
                  props:
                    - name: cpu
                      props:
                        - name: percent
                          value: integer
            - name: termination
              props:
                - name: grace_period_seconds
                  value: integer
        - name: functions
          value: array
          props:
            - name: cors
              props:
                - name: allow_origins
                  value: array
                  props:
                    - name: exact
                      value: string
                    - name: prefix
                      value: string
                    - name: regex
                      value: string
                - name: allow_methods
                  value: array
                - name: allow_headers
                  value: array
                - name: expose_headers
                  value: array
                - name: max_age
                  value: string
                - name: allow_credentials
                  value: boolean
            - name: routes
              value: array
              props:
                - name: path
                  value: string
                - name: preserve_path_prefix
                  value: boolean
            - name: name
              value: string
            - name: source_dir
              value: string
            - name: alerts
              value: array
              props:
                - name: rule
                  value: string
                - name: disabled
                  value: boolean
                - name: operator
                  value: string
                - name: value
                  value: number
                - name: window
                  value: string
            - name: envs
              value: array
              props:
                - name: key
                  value: string
                - name: scope
                  value: string
                - name: type
                  value: string
                - name: value
                  value: string
            - name: git
              props:
                - name: branch
                  value: string
                - name: repo_clone_url
                  value: string
            - name: github
              props:
                - name: branch
                  value: string
                - name: deploy_on_push
                  value: boolean
                - name: repo
                  value: string
            - name: gitlab
              props:
                - name: branch
                  value: string
                - name: deploy_on_push
                  value: boolean
                - name: repo
                  value: string
            - name: log_destinations
              value: array
              props:
                - name: name
                  value: string
                - name: papertrail
                  props:
                    - name: endpoint
                      value: string
                - name: datadog
                  props:
                    - name: endpoint
                      value: string
                    - name: api_key
                      value: string
                - name: logtail
                  props:
                    - name: token
                      value: string
                - name: open_search
                  props:
                    - name: endpoint
                      value: string
                    - name: basic_auth
                      props:
                        - name: user
                          value: string
                        - name: password
                          value: string
                    - name: index_name
                      value: string
                    - name: cluster_name
                      value: string
        - name: databases
          value: array
          props:
            - name: cluster_name
              value: string
            - name: db_name
              value: string
            - name: db_user
              value: string
            - name: engine
              value: string
            - name: name
              value: string
            - name: production
              value: boolean
            - name: version
              value: string
        - name: ingress
          props:
            - name: rules
              value: array
              props:
                - name: match
                  props:
                    - name: path
                      props:
                        - name: prefix
                          value: string
                - name: cors
                  props:
                    - name: allow_origins
                      value: array
                      props:
                        - name: exact
                          value: string
                        - name: prefix
                          value: string
                        - name: regex
                          value: string
                    - name: allow_methods
                      value: array
                    - name: allow_headers
                      value: array
                    - name: expose_headers
                      value: array
                    - name: max_age
                      value: string
                    - name: allow_credentials
                      value: boolean
                - name: component
                  props:
                    - name: name
                      value: string
                    - name: preserve_path_prefix
                      value: string
                    - name: rewrite
                      value: string
                - name: redirect
                  props:
                    - name: uri
                      value: string
                    - name: authority
                      value: string
                    - name: port
                      value: integer
                    - name: scheme
                      value: string
                    - name: redirect_code
                      value: integer
        - name: egress
          props:
            - name: type
              value: string
        - name: maintenance
          props:
            - name: enabled
              value: boolean
            - name: archive
              value: boolean
    - name: project_id
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>apps</code> resource.

```sql
/*+ delete */
DELETE FROM digitalocean.apps.apps
WHERE id = '{{ id }}';
```
