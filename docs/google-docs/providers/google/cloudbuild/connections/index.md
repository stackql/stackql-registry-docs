---
title: connections
hide_title: false
hide_table_of_contents: false
keywords:
  - connections
  - cloudbuild
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

Creates, updates, deletes, gets or lists a <code>connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudbuild.connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The resource name of the connection, in the format `projects/{project}/locations/{location}/connections/{connection_id}`. |
| <CopyableCode code="annotations" /> | `object` | Optional. Allows clients to store small amounts of arbitrary data. |
| <CopyableCode code="bitbucketCloudConfig" /> | `object` | Configuration for connections to Bitbucket Cloud. |
| <CopyableCode code="bitbucketDataCenterConfig" /> | `object` | Configuration for connections to Bitbucket Data Center. |
| <CopyableCode code="createTime" /> | `string` | Output only. Server assigned timestamp for when the connection was created. |
| <CopyableCode code="disabled" /> | `boolean` | Optional. If disabled is set to true, functionality is disabled for this connection. Repository based API methods and webhooks processing for repositories in this connection will be disabled. |
| <CopyableCode code="etag" /> | `string` | This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| <CopyableCode code="githubConfig" /> | `object` | Configuration for connections to github.com. |
| <CopyableCode code="githubEnterpriseConfig" /> | `object` | Configuration for connections to an instance of GitHub Enterprise. |
| <CopyableCode code="gitlabConfig" /> | `object` | Configuration for connections to gitlab.com or an instance of GitLab Enterprise. |
| <CopyableCode code="installationState" /> | `object` | Describes stage and necessary actions to be taken by the user to complete the installation. Used for GitHub and GitHub Enterprise based connections. |
| <CopyableCode code="reconciling" /> | `boolean` | Output only. Set to true when the connection is being set up or updated in the background. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Server assigned timestamp for when the connection was updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_connections_get" /> | `SELECT` | <CopyableCode code="connectionsId, locationsId, projectsId" /> | Gets details of a single connection. |
| <CopyableCode code="projects_locations_connections_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists Connections in a given project and location. |
| <CopyableCode code="projects_locations_connections_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a Connection. |
| <CopyableCode code="projects_locations_connections_delete" /> | `DELETE` | <CopyableCode code="connectionsId, locationsId, projectsId" /> | Deletes a single connection. |
| <CopyableCode code="projects_locations_connections_patch" /> | `UPDATE` | <CopyableCode code="connectionsId, locationsId, projectsId" /> | Updates a single connection. |
| <CopyableCode code="projects_locations_connections_process_webhook" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | ProcessWebhook is called by the external SCM for notifying of events. |

## `SELECT` examples

Lists Connections in a given project and location.

```sql
SELECT
name,
annotations,
bitbucketCloudConfig,
bitbucketDataCenterConfig,
createTime,
disabled,
etag,
githubConfig,
githubEnterpriseConfig,
gitlabConfig,
installationState,
reconciling,
updateTime
FROM google.cloudbuild.connections
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>connections</code> resource.

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
INSERT INTO google.cloudbuild.connections (
locationsId,
projectsId,
githubEnterpriseConfig,
bitbucketDataCenterConfig,
bitbucketCloudConfig,
annotations,
etag,
githubConfig,
disabled,
name,
gitlabConfig
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ githubEnterpriseConfig }}',
'{{ bitbucketDataCenterConfig }}',
'{{ bitbucketCloudConfig }}',
'{{ annotations }}',
'{{ etag }}',
'{{ githubConfig }}',
{{ disabled }},
'{{ name }}',
'{{ gitlabConfig }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: githubEnterpriseConfig
      value:
        - name: hostUri
          value: string
        - name: appId
          value: string
        - name: privateKeySecretVersion
          value: string
        - name: webhookSecretSecretVersion
          value: string
        - name: appInstallationId
          value: string
        - name: appSlug
          value: string
        - name: serverVersion
          value: string
        - name: apiKey
          value: string
        - name: serviceDirectoryConfig
          value:
            - name: service
              value: string
        - name: sslCa
          value: string
    - name: updateTime
      value: string
    - name: bitbucketDataCenterConfig
      value:
        - name: readAuthorizerCredential
          value:
            - name: userTokenSecretVersion
              value: string
            - name: username
              value: string
        - name: hostUri
          value: string
        - name: webhookSecretSecretVersion
          value: string
        - name: serverVersion
          value: string
        - name: sslCa
          value: string
    - name: bitbucketCloudConfig
      value:
        - name: webhookSecretSecretVersion
          value: string
        - name: workspace
          value: string
    - name: annotations
      value: object
    - name: etag
      value: string
    - name: githubConfig
      value:
        - name: appInstallationId
          value: string
        - name: authorizerCredential
          value:
            - name: oauthTokenSecretVersion
              value: string
            - name: username
              value: string
    - name: disabled
      value: boolean
    - name: installationState
      value:
        - name: stage
          value: string
        - name: actionUri
          value: string
        - name: message
          value: string
    - name: name
      value: string
    - name: reconciling
      value: boolean
    - name: createTime
      value: string
    - name: gitlabConfig
      value:
        - name: serverVersion
          value: string
        - name: webhookSecretSecretVersion
          value: string
        - name: sslCa
          value: string
        - name: hostUri
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>connections</code> resource.

```sql
/*+ update */
UPDATE google.cloudbuild.connections
SET 
githubEnterpriseConfig = '{{ githubEnterpriseConfig }}',
bitbucketDataCenterConfig = '{{ bitbucketDataCenterConfig }}',
bitbucketCloudConfig = '{{ bitbucketCloudConfig }}',
annotations = '{{ annotations }}',
etag = '{{ etag }}',
githubConfig = '{{ githubConfig }}',
disabled = true|false,
name = '{{ name }}',
gitlabConfig = '{{ gitlabConfig }}'
WHERE 
connectionsId = '{{ connectionsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>connections</code> resource.

```sql
/*+ delete */
DELETE FROM google.cloudbuild.connections
WHERE connectionsId = '{{ connectionsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
