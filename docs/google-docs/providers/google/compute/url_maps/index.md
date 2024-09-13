
---
title: url_maps
hide_title: false
hide_table_of_contents: false
keywords:
  - url_maps
  - compute
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

Creates, updates, deletes or gets an <code>url_map</code> resource or lists <code>url_maps</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>url_maps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.url_maps" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| <CopyableCode code="name" /> | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| <CopyableCode code="description" /> | `string` | An optional description of this resource. Provide this property when you create the resource. |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| <CopyableCode code="defaultCustomErrorResponsePolicy" /> | `object` | Specifies the custom error response policy that must be applied when the backend service or backend bucket responds with an error. |
| <CopyableCode code="defaultRouteAction" /> | `object` |  |
| <CopyableCode code="defaultService" /> | `string` | The full or partial URL of the defaultService resource to which traffic is directed if none of the hostRules match. If defaultRouteAction is also specified, advanced routing actions, such as URL rewrites, take effect before sending the request to the backend. However, if defaultService is specified, defaultRouteAction cannot contain any defaultRouteAction.weightedBackendServices. Conversely, if defaultRouteAction specifies any defaultRouteAction.weightedBackendServices, defaultService must not be specified. If defaultService is specified, then set either defaultUrlRedirect , or defaultRouteAction.weightedBackendService Don't set both. defaultService has no effect when the URL map is bound to a target gRPC proxy that has the validateForProxyless field set to true. |
| <CopyableCode code="defaultUrlRedirect" /> | `object` | Specifies settings for an HTTP redirect. |
| <CopyableCode code="fingerprint" /> | `string` | Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking. This field is ignored when inserting a UrlMap. An up-to-date fingerprint must be provided in order to update the UrlMap, otherwise the request will fail with error 412 conditionNotMet. To see the latest fingerprint, make a get() request to retrieve a UrlMap. |
| <CopyableCode code="headerAction" /> | `object` | The request and response header transformations that take effect before the request is passed along to the selected backendService. |
| <CopyableCode code="hostRules" /> | `array` | The list of host rules to use against the URL. |
| <CopyableCode code="kind" /> | `string` | [Output Only] Type of the resource. Always compute#urlMaps for url maps. |
| <CopyableCode code="pathMatchers" /> | `array` | The list of named PathMatchers to use against the URL. |
| <CopyableCode code="region" /> | `string` | [Output Only] URL of the region where the regional URL map resides. This field is not applicable to global URL maps. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined URL for the resource. |
| <CopyableCode code="tests" /> | `array` | The list of expected URL mapping tests. Request to update the UrlMap succeeds only if all test cases pass. You can specify a maximum of 100 tests per UrlMap. Not supported when the URL map is bound to a target gRPC proxy that has validateForProxyless field set to true. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="project, urlMap" /> | Returns the specified UrlMap resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project" /> | Retrieves the list of UrlMap resources available to the specified project. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="project" /> | Creates a UrlMap resource in the specified project using the data included in the request. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="project, urlMap" /> | Deletes the specified UrlMap resource. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="project, urlMap" /> | Patches the specified UrlMap resource with the data included in the request. This method supports PATCH semantics and uses the JSON merge patch format and processing rules. |
| <CopyableCode code="invalidate_cache" /> | `EXEC` | <CopyableCode code="project, urlMap" /> | Initiates a cache invalidation operation, invalidating the specified path, scoped to the specified UrlMap. For more information, see [Invalidating cached content](/cdn/docs/invalidating-cached-content). |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="project, urlMap" /> | Updates the specified UrlMap resource with the data included in the request. |
| <CopyableCode code="validate" /> | `EXEC` | <CopyableCode code="project, urlMap" /> | Runs static validation for the UrlMap. In particular, the tests of the provided UrlMap will be run. Calling this method does NOT create the UrlMap. |

## `SELECT` examples

Retrieves the list of UrlMap resources available to the specified project.

```sql
SELECT
id,
name,
description,
creationTimestamp,
defaultCustomErrorResponsePolicy,
defaultRouteAction,
defaultService,
defaultUrlRedirect,
fingerprint,
headerAction,
hostRules,
kind,
pathMatchers,
region,
selfLink,
tests
FROM google.compute.url_maps
WHERE project = '{{ project }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>url_maps</code> resource.

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
INSERT INTO google.compute.url_maps (
project,
kind,
id,
creationTimestamp,
name,
description,
selfLink,
hostRules,
pathMatchers,
tests,
defaultService,
defaultRouteAction,
defaultUrlRedirect,
headerAction,
defaultCustomErrorResponsePolicy,
fingerprint,
region
)
SELECT 
'{{ project }}',
'{{ kind }}',
'{{ id }}',
'{{ creationTimestamp }}',
'{{ name }}',
'{{ description }}',
'{{ selfLink }}',
'{{ hostRules }}',
'{{ pathMatchers }}',
'{{ tests }}',
'{{ defaultService }}',
'{{ defaultRouteAction }}',
'{{ defaultUrlRedirect }}',
'{{ headerAction }}',
'{{ defaultCustomErrorResponsePolicy }}',
'{{ fingerprint }}',
'{{ region }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: kind
        value: '{{ kind }}'
      - name: id
        value: '{{ id }}'
      - name: creationTimestamp
        value: '{{ creationTimestamp }}'
      - name: name
        value: '{{ name }}'
      - name: description
        value: '{{ description }}'
      - name: selfLink
        value: '{{ selfLink }}'
      - name: hostRules
        value: '{{ hostRules }}'
      - name: pathMatchers
        value: '{{ pathMatchers }}'
      - name: tests
        value: '{{ tests }}'
      - name: defaultService
        value: '{{ defaultService }}'
      - name: defaultRouteAction
        value: '{{ defaultRouteAction }}'
      - name: defaultUrlRedirect
        value: '{{ defaultUrlRedirect }}'
      - name: headerAction
        value: '{{ headerAction }}'
      - name: defaultCustomErrorResponsePolicy
        value: '{{ defaultCustomErrorResponsePolicy }}'
      - name: fingerprint
        value: '{{ fingerprint }}'
      - name: region
        value: '{{ region }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a url_map only if the necessary resources are available.

```sql
UPDATE google.compute.url_maps
SET 
kind = '{{ kind }}',
id = '{{ id }}',
creationTimestamp = '{{ creationTimestamp }}',
name = '{{ name }}',
description = '{{ description }}',
selfLink = '{{ selfLink }}',
hostRules = '{{ hostRules }}',
pathMatchers = '{{ pathMatchers }}',
tests = '{{ tests }}',
defaultService = '{{ defaultService }}',
defaultRouteAction = '{{ defaultRouteAction }}',
defaultUrlRedirect = '{{ defaultUrlRedirect }}',
headerAction = '{{ headerAction }}',
defaultCustomErrorResponsePolicy = '{{ defaultCustomErrorResponsePolicy }}',
fingerprint = '{{ fingerprint }}',
region = '{{ region }}'
WHERE 
project = '{{ project }}'
AND urlMap = '{{ urlMap }}';
```

## `DELETE` example

Deletes the specified url_map resource.

```sql
DELETE FROM google.compute.url_maps
WHERE project = '{{ project }}'
AND urlMap = '{{ urlMap }}';
```
