/*
 *  Copyright 2024 Collate.
 *  Licensed under the Apache License, Version 2.0 (the "License");
 *  you may not use this file except in compliance with the License.
 *  You may obtain a copy of the License at
 *  http://www.apache.org/licenses/LICENSE-2.0
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 */
import { Col, Row, Space } from 'antd';
import { capitalize } from 'lodash';
import React, { useCallback, useMemo } from 'react';
import { useTranslation } from 'react-i18next';
import { useHistory, useParams } from 'react-router-dom';
import TitleBreadcrumb from '../../../components/common/TitleBreadcrumb/TitleBreadcrumb.component';
import { TitleBreadcrumbProps } from '../../../components/common/TitleBreadcrumb/TitleBreadcrumb.interface';
import PageHeader from '../../../components/PageHeader/PageHeader.component';
import PageLayoutV1 from '../../../components/PageLayoutV1/PageLayoutV1';
import { usePermissionProvider } from '../../../components/PermissionProvider/PermissionProvider';
import SettingItemCard from '../../../components/Setting/SettingItemCard/SettingItemCard.component';
import { ROUTES } from '../../../constants/constants';
import {
  GlobalSettingOptions,
  GlobalSettingsMenuCategory,
} from '../../../constants/GlobalSettings.constants';
import { PAGE_HEADERS } from '../../../constants/PageHeaders.constant';
import { ELASTIC_SEARCH_RE_INDEX_PAGE_TABS } from '../../../enums/ElasticSearch.enum';
import { TeamType } from '../../../generated/entity/teams/team';
import { useAuth } from '../../../hooks/authHooks';
import {
  getGlobalSettingsMenuWithPermission,
  SettingMenuItem,
} from '../../../utils/GlobalSettingsUtils';
import {
  getSettingPath,
  getSettingsPathWithFqn,
  getTeamsWithFqnPath,
} from '../../../utils/RouterUtils';

const GlobalSettingCategoryPage = () => {
  const { t } = useTranslation();
  const history = useHistory();
  const { settingCategory } = useParams<{ settingCategory: string }>();
  const { permissions } = usePermissionProvider();
  const { isAdminUser } = useAuth();

  const breadcrumbs: TitleBreadcrumbProps['titleLinks'] = useMemo(
    () => [
      {
        name: t('label.setting-plural'),
        url: ROUTES.SETTINGS,
        activeTitle: false,
      },
      {
        name: capitalize(settingCategory),
        url: '',
        activeTitle: true,
      },
    ],
    [settingCategory]
  );

  const handleSettingItemClick = useCallback((key: string) => {
    const [category, option] = key.split('.');

    switch (option) {
      case GlobalSettingOptions.TEAMS:
        history.push(getTeamsWithFqnPath(TeamType.Organization));

        break;
      case GlobalSettingOptions.SEARCH:
        if (category === GlobalSettingsMenuCategory.OPEN_METADATA) {
          history.push(
            getSettingsPathWithFqn(
              category,
              option,
              ELASTIC_SEARCH_RE_INDEX_PAGE_TABS.ON_DEMAND
            )
          );
        } else {
          history.push(getSettingPath(category, option));
        }

        break;
      default:
        history.push(getSettingPath(category, option));

        break;
    }
  }, []);

  const categoryItems: SettingMenuItem[] = useMemo(
    () =>
      getGlobalSettingsMenuWithPermission(permissions, isAdminUser).find(
        (item) => item.key === settingCategory
      )?.items || [],

    [settingCategory, permissions, isAdminUser]
  );

  return (
    <PageLayoutV1 pageTitle={t('label.setting-plural')}>
      <Row className="page-container" gutter={[0, 20]}>
        <Col span={24}>
          <TitleBreadcrumb titleLinks={breadcrumbs} />
        </Col>

        <Col span={24}>
          <Space className="w-full d-flex justify-between">
            <PageHeader data={PAGE_HEADERS.SETTING} />
          </Space>
        </Col>

        <Col span={24}>
          <Row gutter={[20, 20]}>
            {categoryItems.map((category) => (
              <Col key={category?.key} span={6}>
                <SettingItemCard
                  data={category}
                  onClick={handleSettingItemClick}
                />
              </Col>
            ))}
          </Row>
        </Col>
      </Row>
    </PageLayoutV1>
  );
};

export default GlobalSettingCategoryPage;
