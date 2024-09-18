---
title: apiproducts
hide_title: false
hide_table_of_contents: false
keywords:
  - apiproducts
  - apigee
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

Creates, updates, deletes, gets or lists a <code>apiproducts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>apiproducts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.apiproducts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Internal name of the API product. Characters you can use in the name are restricted to: `A-Z0-9._\-$ %`. **Note:** The internal name cannot be edited when updating the API product. |
| <CopyableCode code="description" /> | `string` | Description of the API product. Include key information about the API product that is not captured by other fields. |
| <CopyableCode code="apiResources" /> | `array` | Comma-separated list of API resources to be bundled in the API product. By default, the resource paths are mapped from the `proxy.pathsuffix` variable. The proxy path suffix is defined as the URI fragment following the ProxyEndpoint base path. For example, if the `apiResources` element is defined to be `/forecastrss` and the base path defined for the API proxy is `/weather`, then only requests to `/weather/forecastrss` are permitted by the API product. You can select a specific path, or you can select all subpaths with the following wildcard: - `/**`: Indicates that all sub-URIs are included. - `/*` : Indicates that only URIs one level down are included. By default, / supports the same resources as /** as well as the base path defined by the API proxy. For example, if the base path of the API proxy is `/v1/weatherapikey`, then the API product supports requests to `/v1/weatherapikey` and to any sub-URIs, such as `/v1/weatherapikey/forecastrss`, `/v1/weatherapikey/region/CA`, and so on. For more information, see Managing API products. |
| <CopyableCode code="approvalType" /> | `string` | Flag that specifies how API keys are approved to access the APIs defined by the API product. If set to `manual`, the consumer key is generated and returned in "pending" state. In this case, the API keys won't work until they have been explicitly approved. If set to `auto`, the consumer key is generated and returned in "approved" state and can be used immediately. **Note:** Typically, `auto` is used to provide access to free or trial API products that provide limited quota or capabilities. |
| <CopyableCode code="attributes" /> | `array` | Array of attributes that may be used to extend the default API product profile with customer-specific metadata. You can specify a maximum of 18 attributes. Use this property to specify the access level of the API product as either `public`, `private`, or `internal`. Only products marked `public` are available to developers in the Apigee developer portal. For example, you can set a product to `internal` while it is in development and then change access to `public` when it is ready to release on the portal. API products marked as `private` do not appear on the portal, but can be accessed by external developers. |
| <CopyableCode code="createdAt" /> | `string` | Response only. Creation time of this environment as milliseconds since epoch. |
| <CopyableCode code="displayName" /> | `string` | Name displayed in the UI or developer portal to developers registering for API access. |
| <CopyableCode code="environments" /> | `array` | Comma-separated list of environment names to which the API product is bound. Requests to environments that are not listed are rejected. By specifying one or more environments, you can bind the resources listed in the API product to a specific environment, preventing developers from accessing those resources through API proxies deployed in another environment. This setting is used, for example, to prevent resources associated with API proxies in `prod` from being accessed by API proxies deployed in `test`. |
| <CopyableCode code="graphqlOperationGroup" /> | `object` | List of graphQL operation configuration details associated with Apigee API proxies or remote services. Remote services are non-Apigee proxies, such as Istio-Envoy. |
| <CopyableCode code="grpcOperationGroup" /> | `object` | List of gRPC operation configuration details associated with Apigee API proxies. |
| <CopyableCode code="lastModifiedAt" /> | `string` | Response only. Modified time of this environment as milliseconds since epoch. |
| <CopyableCode code="operationGroup" /> | `object` | List of operation configuration details associated with Apigee API proxies or remote services. Remote services are non-Apigee proxies, such as Istio-Envoy. |
| <CopyableCode code="proxies" /> | `array` | Comma-separated list of API proxy names to which this API product is bound. By specifying API proxies, you can associate resources in the API product with specific API proxies, preventing developers from accessing those resources through other API proxies. Apigee rejects requests to API proxies that are not listed. **Note:** The API proxy names must already exist in the specified environment as they will be validated upon creation. |
| <CopyableCode code="quota" /> | `string` | Number of request messages permitted per app by this API product for the specified `quotaInterval` and `quotaTimeUnit`. For example, a `quota` of 50, for a `quotaInterval` of 12 and a `quotaTimeUnit` of hours means 50 requests are allowed every 12 hours. |
| <CopyableCode code="quotaCounterScope" /> | `string` | Scope of the quota decides how the quota counter gets applied and evaluate for quota violation. If the Scope is set as PROXY, then all the operations defined for the APIproduct that are associated with the same proxy will share the same quota counter set at the APIproduct level, making it a global counter at a proxy level. If the Scope is set as OPERATION, then each operations get the counter set at the API product dedicated, making it a local counter. Note that, the QuotaCounterScope applies only when an operation does not have dedicated quota set for itself. |
| <CopyableCode code="quotaInterval" /> | `string` | Time interval over which the number of request messages is calculated. |
| <CopyableCode code="quotaTimeUnit" /> | `string` | Time unit defined for the `quotaInterval`. Valid values include `minute`, `hour`, `day`, or `month`. |
| <CopyableCode code="scopes" /> | `array` | Comma-separated list of OAuth scopes that are validated at runtime. Apigee validates that the scopes in any access token presented match the scopes defined in the OAuth policy associated with the API product. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_apiproducts_get" /> | `SELECT` | <CopyableCode code="apiproductsId, organizationsId" /> | Gets configuration details for an API product. The API product name required in the request URL is the internal name of the product, not the display name. While they may be the same, it depends on whether the API product was created via the UI or the API. View the list of API products to verify the internal name. |
| <CopyableCode code="organizations_apiproducts_list" /> | `SELECT` | <CopyableCode code="organizationsId" /> | Lists all API product names for an organization. Filter the list by passing an `attributename` and `attibutevalue`. The maximum number of API products returned is 1000. You can paginate the list of API products returned using the `startKey` and `count` query parameters. |
| <CopyableCode code="organizations_apiproducts_create" /> | `INSERT` | <CopyableCode code="organizationsId" /> | Creates an API product in an organization. You create API products after you have proxied backend services using API proxies. An API product is a collection of API resources combined with quota settings and metadata that you can use to deliver customized and productized API bundles to your developer community. This metadata can include: - Scope - Environments - API proxies - Extensible profile API products enable you repackage APIs on the fly, without having to do any additional coding or configuration. Apigee recommends that you start with a simple API product including only required elements. You then provision credentials to apps to enable them to start testing your APIs. After you have authentication and authorization working against a simple API product, you can iterate to create finer-grained API products, defining different sets of API resources for each API product. **WARNING:** - If you don't specify an API proxy in the request body, *any* app associated with the product can make calls to *any* API in your entire organization. - If you don't specify an environment in the request body, the product allows access to all environments. For more information, see What is an API product? |
| <CopyableCode code="organizations_apiproducts_delete" /> | `DELETE` | <CopyableCode code="apiproductsId, organizationsId" /> | Deletes an API product from an organization. Deleting an API product causes app requests to the resource URIs defined in the API product to fail. Ensure that you create a new API product to serve existing apps, unless your intention is to disable access to the resources defined in the API product. The API product name required in the request URL is the internal name of the product, not the display name. While they may be the same, it depends on whether the API product was created via the UI or the API. View the list of API products to verify the internal name. |
| <CopyableCode code="organizations_appgroups_apps_keys_apiproducts_delete" /> | `DELETE` | <CopyableCode code="apiproductsId, appgroupsId, appsId, keysId, organizationsId" /> | Removes an API product from an app's consumer key. After the API product is removed, the app cannot access the API resources defined in that API product. **Note**: The consumer key is not removed, only its association with the API product. |
| <CopyableCode code="organizations_developers_apps_keys_apiproducts_delete" /> | `DELETE` | <CopyableCode code="apiproductsId, appsId, developersId, keysId, organizationsId" /> | Removes an API product from an app's consumer key. After the API product is removed, the app cannot access the API resources defined in that API product. **Note**: The consumer key is not removed, only its association with the API product. |
| <CopyableCode code="organizations_apiproducts_update" /> | `REPLACE` | <CopyableCode code="apiproductsId, organizationsId" /> | Updates an existing API product. You must include all required values, whether or not you are updating them, as well as any optional values that you are updating. The API product name required in the request URL is the internal name of the product, not the display name. While they may be the same, it depends on whether the API product was created via UI or API. View the list of API products to identify their internal names. |
| <CopyableCode code="organizations_apiproducts_attributes" /> | `EXEC` | <CopyableCode code="apiproductsId, organizationsId" /> | Updates or creates API product attributes. This API **replaces** the current list of attributes with the attributes specified in the request body. In this way, you can update existing attributes, add new attributes, or delete existing attributes by omitting them from the request body. **Note**: OAuth access tokens and Key Management Service (KMS) entities (apps, developers, and API products) are cached for 180 seconds (current default). Any custom attributes associated with entities also get cached for at least 180 seconds after entity is accessed during runtime. In this case, the `ExpiresIn` element on the OAuthV2 policy won't be able to expire an access token in less than 180 seconds. |

## `SELECT` examples

Lists all API product names for an organization. Filter the list by passing an `attributename` and `attibutevalue`. The maximum number of API products returned is 1000. You can paginate the list of API products returned using the `startKey` and `count` query parameters.

```sql
SELECT
name,
description,
apiResources,
approvalType,
attributes,
createdAt,
displayName,
environments,
graphqlOperationGroup,
grpcOperationGroup,
lastModifiedAt,
operationGroup,
proxies,
quota,
quotaCounterScope,
quotaInterval,
quotaTimeUnit,
scopes
FROM google.apigee.apiproducts
WHERE organizationsId = '{{ organizationsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>apiproducts</code> resource.

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
INSERT INTO google.apigee.apiproducts (
organizationsId,
displayName,
scopes,
apiResources,
quotaInterval,
proxies,
createdAt,
approvalType,
name,
attributes,
grpcOperationGroup,
quotaTimeUnit,
description,
quota,
lastModifiedAt,
environments,
graphqlOperationGroup,
operationGroup,
quotaCounterScope
)
SELECT 
'{{ organizationsId }}',
'{{ displayName }}',
'{{ scopes }}',
'{{ apiResources }}',
'{{ quotaInterval }}',
'{{ proxies }}',
'{{ createdAt }}',
'{{ approvalType }}',
'{{ name }}',
'{{ attributes }}',
'{{ grpcOperationGroup }}',
'{{ quotaTimeUnit }}',
'{{ description }}',
'{{ quota }}',
'{{ lastModifiedAt }}',
'{{ environments }}',
'{{ graphqlOperationGroup }}',
'{{ operationGroup }}',
'{{ quotaCounterScope }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
displayName: string
scopes:
  - type: string
apiResources:
  - type: string
quotaInterval: string
proxies:
  - type: string
createdAt: string
approvalType: string
name: string
attributes:
  - value: string
    name: string
grpcOperationGroup:
  operationConfigs:
    - methods:
        - type: string
      apiSource: string
      quota:
        interval: string
        limit: string
        timeUnit: string
      attributes:
        - value: string
          name: string
      service: string
quotaTimeUnit: string
description: string
quota: string
lastModifiedAt: string
environments:
  - type: string
graphqlOperationGroup:
  operationConfigs:
    - attributes:
        - value: string
          name: string
      operations:
        - operation: string
          operationTypes:
            - type: string
      apiSource: string
  operationConfigType: string
operationGroup:
  operationConfigType: string
  operationConfigs:
    - operations:
        - methods:
            - type: string
          resource: string
      apiSource: string
      attributes:
        - value: string
          name: string
quotaCounterScope: string

```
</TabItem>
</Tabs>

## `REPLACE` example

Replaces all fields in the specified <code>apiproducts</code> resource.

```sql
/*+ update */
REPLACE google.apigee.apiproducts
SET 
displayName = '{{ displayName }}',
scopes = '{{ scopes }}',
apiResources = '{{ apiResources }}',
quotaInterval = '{{ quotaInterval }}',
proxies = '{{ proxies }}',
createdAt = '{{ createdAt }}',
approvalType = '{{ approvalType }}',
name = '{{ name }}',
attributes = '{{ attributes }}',
grpcOperationGroup = '{{ grpcOperationGroup }}',
quotaTimeUnit = '{{ quotaTimeUnit }}',
description = '{{ description }}',
quota = '{{ quota }}',
lastModifiedAt = '{{ lastModifiedAt }}',
environments = '{{ environments }}',
graphqlOperationGroup = '{{ graphqlOperationGroup }}',
operationGroup = '{{ operationGroup }}',
quotaCounterScope = '{{ quotaCounterScope }}'
WHERE 
apiproductsId = '{{ apiproductsId }}'
AND organizationsId = '{{ organizationsId }}';
```

## `DELETE` example

Deletes the specified <code>apiproducts</code> resource.

```sql
/*+ delete */
DELETE FROM google.apigee.apiproducts
WHERE apiproductsId = '{{ apiproductsId }}'
AND organizationsId = '{{ organizationsId }}';
```
