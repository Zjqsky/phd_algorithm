from app import app

# 配置路由，不能删
import urls

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9001)

